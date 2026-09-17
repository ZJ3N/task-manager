from datetime import datetime

from pydantic import BaseModel

from app.enums import Priority, Role, Status


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: Role
    is_active: bool


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class TaskResponse(BaseModel):
    id: int
    title: str
    priority: Priority
    status: Status
    due_date: datetime | None
    date_created: datetime
    user_id: int