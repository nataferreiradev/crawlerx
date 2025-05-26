from pydantic import BaseModel, Field
from typing import Optional

class ScriptJsonObject(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., max_length=255)
    url: Optional[str] = Field(default="", max_length=255)
    path: Optional[str] = Field(default="", max_length=255) 
    return_type: str = Field(..., max_length=10)