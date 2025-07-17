from pydantic import BaseModel


class StatusCodesSchema(BaseModel):
    """
    Описание структуры ответа.
    """
    description: str
    statusCode: int
