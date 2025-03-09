from typing import Optional
from beanie import Document
from pydantic import EmailStr
from datetime import datetime
from enum import Enum

from server.core.types import string

class CourseEntity(Document):
    author: string
    title: string
    total_lessons: int
    total_learned: int
    total_exercises: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None
    
    class Settings:
        name = "courses"