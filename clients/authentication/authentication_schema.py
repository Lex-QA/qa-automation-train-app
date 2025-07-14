from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    model_config = ConfigDict(populate_by_name=True)

    password: str = Field(default_factory=fake.password)
    username: str = Field(default_factory=fake.text)


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: str = Field(alias="token")
