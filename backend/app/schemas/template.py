from contextlib import nullcontext
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class PostRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    slug: str
    title: str
    excerpt: str
    body_md: str
    cover_image_url: str | None
    status: str
    published_at: datetime | None
    notion_last_edited_at: datetime

class PostListItem(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id: UUID
    slug: str
    title: str
    excerpt: str
    cover_image_url: str | None
    published_at: datetime | None