from datetime import datetime
from typing import (
    Dict,
    TypeVar,
    Generic,
    List,
    Optional,
    Type,
    Any,
    Mapping,
    Tuple,
    Union,
)
from server.core.types import string
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from server.core.https import Meta
from server.domain.entities.base_entity import BaseEntity

T = TypeVar("T", bound=BaseEntity)

class BaseRepository(Generic[T]):
    def __init__(self, collection: AsyncIOMotorCollection, model: Type[T]):
        self.collection = collection
        self.model = model

    def _convert_id(self, doc: Dict[str, Any]) -> Dict[str, Any]:
        result = dict(doc)
        if "_id" in result:
            result["id"] = str(result["_id"])

        return result

    def _convert_doc(self, doc: Dict[str, Any]) -> T:
        converted = self._convert_id(doc)
        return self.model.model_validate(converted)

    def _convert_entities(self, docs: List[Dict[str, Any]]) -> List[T]:
        return [self._convert_doc(doc) for doc in docs]

    async def find_with_options(
        self,
        *args: Mapping[str, Any],
    ) -> List[T]:
        docs = await self.collection.find(*args).to_list()
        data = self._convert_entities(docs)

        return data

    async def find_pagination(
        self,
        *args: Mapping[str, Any],
        page: int,
        page_size: int,
    ) -> Tuple[List[T], Meta]:
        skip = (page - 1) * page_size

        query = self.collection.find(*args).skip(skip).limit(page_size)
        docs = await query.to_list()

        total_record = await self.collection.count_documents(filter=args[0])
        total_page = (total_record + page_size - 1) // page_size

        meta = Meta(
            page=page,
            page_size=page_size,
            total_page=total_page,
            total_record=total_record,
        )

        data = self._convert_entities(docs)
        return data, meta

    async def create(self, entity: T) -> T:
        data = entity.model_dump(exclude={"id"}, exclude_unset=True)
        result = await self.collection.insert_one(data)

        data["id"] = str(result.inserted_id)
        return self.model.model_validate(data)

    async def update(self, id: string, data: Dict[str, Any]) -> Optional[T]:
        if not ObjectId.is_valid(id):
            return None

        entity = await self.collection.find_one({"_id": ObjectId(id)})
        if not entity:
            return None

        if isinstance(data, BaseEntity):
            update_data = data.model_dump(exclude_unset=True)
        else:
            update_data = data

        for key, value in update_data.items():
            if hasattr(entity, key) and key != "_id":
                entity[key] = value

        # remove attr id
        delattr(entity, "_id")
        time = datetime.utcnow()
        entity["updated_at"] = time

        print(entity)

        # update data and updated_at
        await self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": entity.model_dump(exclude={"id"}, exclude_unset=True)}
        )

        entity["id"] = id
        return self.model.model_validate(entity)

    async def find_one(self, *args: Mapping[str, Any]) -> Optional[T]:
        response = await self.collection.find_one(*args)
        if response is None:
            return None

        response["id"] = str(response["_id"])
        return self.model.model_validate(response)

    async def delete(self, id: Any) -> Optional[T]:
        doc = await self.collection.find_one({"_id":  ObjectId(id)})
        if not doc:
            return None

        time = datetime.utcnow()
        await self.collection.update_one({"_id": id}, {"$set": {"deleted_at": time}})
        doc["deleted_at"] = time
        return self.model.model_validate(doc)

    async def remove(self, id: Any) -> Optional[T]:
        entity = await self.collection.find_one({"_id": ObjectId(id)})
        if not entity:
            return None

        await entity.delete()
        return entity
