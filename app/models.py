from pydantic import BaseModel
from typing import List, Optional

class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    tags: Optional[List[str]] = []
