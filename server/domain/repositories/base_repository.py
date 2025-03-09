from typing import TypeVar, Generic, List, Optional, Type, Any, Dict
from beanie import Document
from pydantic import BaseModel

T = TypeVar("T", bound=Document)

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

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