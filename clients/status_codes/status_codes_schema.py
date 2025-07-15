from pydantic import BaseModel, HttpUrl, Field, FilePath

from tools.fakers import fake



class StatusCodesSchema(BaseModel):
    """
    Описание структуры ответа.
    """
    description: str
    statusCode: int