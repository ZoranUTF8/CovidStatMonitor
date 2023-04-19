from pydantic import BaseModel, Field


class EmailData(BaseModel):
    name: str = Field(..., title="Name")
    email: str = Field(..., title="Email Address")
    message: str = Field(..., title="Message")
