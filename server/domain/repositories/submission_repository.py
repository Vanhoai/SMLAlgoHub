from bson import ObjectId

from server.database import client
from server.domain.entities.submission_entity import SubmissionEntity
from server.domain.repositories.base_repository import BaseRepository
from server.core.types import string

class SubmissionRepository(BaseRepository[SubmissionEntity]):
    def __init__(self):
        collection = client.get_collection("submissions")
        self.collection = collection
        super().__init__(collection, SubmissionEntity)

    async def create_submission(self, entity: SubmissionEntity) -> SubmissionEntity:
        data = entity.dict(exclude={"id"})
        print("data: ", data)

        for key, value in data.items():
            if "_id" in key:
                data[key] = ObjectId(value)

        result = await self.collection.insert_one(data)
        data["id"] = string(result.inserted_id)

        for key, value in data.items():
            if ObjectId.is_valid(value):
                data[key] = string(value)

        return self.model.validate(data)
