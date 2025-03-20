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
)
from server.core.helpers.time import TimeHelper
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

    async def process_create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        for key, value in data.items():
            if "_id" in key:
                data[key] = ObjectId(value)

        result = await self.collection.insert_one(data)
        data["id"] = string(result.inserted_id)

        for key, value in data.items():
            if ObjectId.is_valid(value):
                data[key] = string(value)

        return data

    async def find_with_options(
        self,
        *args: Mapping[str, Any],
    ) -> List[T]:
        docs = await self.collection.find(*args).to_list()
        return self._convert_entities(docs)

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

        # convert all properties to ObjectId if contain "_id"
        # for key, value in data.items():
        #     if "_id" in key:
        #         data[key] = ObjectId(value)

        print("data insert: ", data)
        result = await self.collection.insert_one(data)

        data["id"] = str(result.inserted_id)

        # reverse all properties ObjectId to string
        # for key, value in data.items():
        #     if "_id" in key:
        #         print(key)
                # data[key] = str(value)
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

        time = TimeHelper.utc_timezone()
        update_data["updated_at"] = time

        await self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_data}
        )

        entity["id"] = id
        entity["updated_at"] = time
        return self.model.model_validate(entity)

    async def find_one(self, *args: Mapping[str, Any]) -> Optional[T]:
        response = await self.collection.find_one(*args)
        if response is None:
            return None

        response["id"] = str(response["_id"])
        return self.model.model_validate(response)

    async def collection_find(self, *args: Mapping[str, Any]) -> Optional[T]:
        response = await self.collection.find_one(*args)
        if response is None:
            return None

        return response

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
