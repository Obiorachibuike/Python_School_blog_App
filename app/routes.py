from fastapi import APIRouter, HTTPException
from app.models import BlogPost
from app.db import database, posts_collection

router = APIRouter()

@router.post("/posts/", response_model=BlogPost)
async def create_post(post: BlogPost):
    post_dict = post.dict()
    result = await posts_collection.insert_one(post_dict)
    post_dict["id"] = str(result.inserted_id)
    return post_dict

@router.get("/posts/", response_model=List[BlogPost])
async def get_all_posts():
    posts = await posts_collection.find().to_list(1000)
    for post in posts:
        post["id"] = str(post["_id"])  # Convert ObjectId to string
        del post["_id"]  # Remove the ObjectId field
    return posts

@router.get("/posts/{post_id}", response_model=BlogPost)
async def get_post(post_id: str):
    post = await posts_collection.find_one({"_id": post_id})
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    post["id"] = str(post["_id"])
    del post["_id"]
    return post

@router.delete("/posts/{post_id}", response_model=dict)
async def delete_post(post_id: str):
    result = await posts_collection.delete_one({"_id": post_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}
