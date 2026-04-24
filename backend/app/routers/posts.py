from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.post import PostRead, PostListItem
from app.crud import post as post_crud

router = APIRouter(prefix="/api/posts", tags=["posts"])

@router.get("", response_model=list[PostListItem])
def list_posts(limit: int = Query(50, le=100), offset: int = 0, db: Session = Depends(get_db)):
    return post_crud.list_published(db, limit=limit, offset=offset)

@router.get("/{slug}", response_model=PostRead)
def get_post(slug: str, db: Session = Depends(get_db)):
    post = post_crud.get_by_slug(db, slug)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post