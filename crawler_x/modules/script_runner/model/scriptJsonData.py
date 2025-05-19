from pydantic import BaseModel, Field
from typing import Optional

class ScriptJsonData(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., max_length=255)
    url: str = Field(..., max_length=255)
    path: str = Field(..., max_length=255)
    return_type: str = Field(..., max_length=10)