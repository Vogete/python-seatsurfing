from pydantic import BaseModel, Field


class PasswordLoginRequest(BaseModel):
    email: str
    password: str
    long_lived: bool = Field(alias="longLived", default=True)


class JWTResponse(BaseModel):
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")
    long_lived: str = Field(alias="longLived")
    logout_url: str = Field(alias="logoutUrl")
