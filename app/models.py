from pydantic import BaseModel
from typing import List

class Video(BaseModel):
    video_id: str
    title: str
    description: str
    video_url: str
    category: List[str]
