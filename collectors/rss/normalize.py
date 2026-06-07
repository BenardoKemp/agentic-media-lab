from pydantic import BaseModel
from typing import Optional

class NewsArticle(BaseModel):

    source: str
    title: str
    link: str
    published: Optional[str]
    summary: Optional[str]



