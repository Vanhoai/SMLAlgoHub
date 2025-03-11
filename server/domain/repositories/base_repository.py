from typing import (
    TypeVar,
    Generic,
    List,
    Optional,
    Type,
    Any,
    Dict,
    Mapping,
    Tuple,
    Union,
)
from beanie import Document
from beanie.odm.enums import SortDirection
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClientSession
from server.core.https import Meta

T = TypeVar("T", bound=Document)


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def find_with_options(
        self,
        *args: Mapping[str, Any],
    ) -> List[T]:
        return await self.model.find(*args).to_list()

    async def find_pagination(
        self,
        *args: Mapping[str, Any],
        page: int,
        page_size: int,
        sort: Union[None, str, List[Tuple[str, SortDirection]]] = None,
    ) -> Tuple[List[T], Meta]:
        skip = (page - 1) * page_size

        query = self.model.find(*args).sort(sort).skip(skip).limit(page_size)
        data = await query.to_list()

        total_record = await self.model.find(*args).count()
        total_page = (total_record + page_size - 1) // page_size

        meta = Meta(
            page=page,
            page_size=page_size,
            total_page=total_page,
            total_record=total_record,
        )

        return data, meta

    async def create(self, data: T) -> T:
        entity = self.model(**data.model_dump())
        await entity.insert()
        return entity

    async def update(self, id: Any, data: T) -> Optional[T]:
        entity = await self.get_by_id(id)
        if not entity:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(entity, key, value)

        await entity.save()
        return entity
