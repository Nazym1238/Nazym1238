import os
import requests

from posts.schemas import CreatePostRequest, EditPostRequest, AddKeywordsRequest
from fastapi import APIRouter
from posts import service

router = APIRouter()


@router.get('')
async def get_posts():
    return await service.get_posts()


@router.post('')
async def create_post(post: CreatePostRequest):
    return await service.create_post(post)


@router.get('/{id}')
async def get_post(id: int):
    return await service.get_post_by_id(id)


@router.put('/{id}')
async def edit_post(id: int, post_data: EditPostRequest):
    return await service.edit_post(id, post_data)


@router.delete('/{id}')
async def delete_post(id: int):
    await service.delete_post(id)

    return {"message": "ok, deleted"}

@router.post('/generate-ad-text')
def genenerate_ad(add_keywords: AddKeywordsRequest):
    token = os.environ.get("TOKEN")

    headers = {
        'Authorization': "Bearer " + token
    }

    response = requests.post('https://7583-185-48-148-173.ngrok-free.app/advertisement', headers=headers, json={
        "input_text": add_keywords.keywords
    })
    
     
    body = response.json()
    return {
        "text": body['output']
    }