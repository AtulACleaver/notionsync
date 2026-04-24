from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.post import Post

def list_published(db: Session, limit: int = 50, offset: int = 0) -> list[Post]:
    stmt = (
        select(Post)
        .where(Post.status == "published")
        .order_by(Post.published_at.desc())
        .limit(limit)
        .offset(offset)
    )
    return list(db.scalars(stmt))

def get_by_slug(db: Session, slug: str) -> Post | None:
    return db.scalar(select(Post).where(Post.slug == slug, Post.status == "published"))