## obejtos jsonData serão usados para a comunicação com o front-end

from pydantic import BaseModel, Field
from typing import Optional, Dict

class ApiJsonData(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., max_length=255)
    url: str = Field(..., max_length=255)
    method: str = Field(..., max_length=10)
    headers: Optional[Dict] = {}
    body: Optional[str] = None
    params: Optional[Dict] = {}
    return_type: str = Field(..., max_length=10)