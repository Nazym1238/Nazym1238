from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class CreatePostRequest(BaseModel):
    author: str
    text: str
    keywords: str



class EditPostRequest(BaseModel):
    author: Optional[str]= None
    text: Optional[str]= None
    keywords: Optional[str]= None



class AddKeywordsRequest(BaseModel):
    keywords: str