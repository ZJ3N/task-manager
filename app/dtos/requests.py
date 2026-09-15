from datetime import datetime

from pydantic import BaseModel, field_validator

from app.enums import Priority


class UserCreateRequest(BaseModel):
    username: str
    email: str
    password: str

    @field_validator("username")
    @classmethod
    def username_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Username cannot be blank")
        return v

    @field_validator("password")
    @classmethod
    def password_min_length(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("Password must be at least 6 characters")
        return v


class TaskCreateRequest(BaseModel):
    title: str
    description: str | None = None
    priority: Priority = Priority.medium
    due_date: datetime | None = None

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Title cannot be empty")
        return v

    @field_validator("due_date")
    @classmethod
    def due_date_not_in_past(cls, v: datetime | None) -> datetime | None:
     if v is not None:
        now = datetime.now(v.tzinfo) if v.tzinfo else datetime.utcnow()
        if v < now:
            raise ValueError("Due date cannot be in the past")
     return v


class TaskUpdateRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: Priority | None = None
    due_date: datetime | None = None

    @field_validator("title")
    @classmethod
    def title_not_blank_if_given(cls, v: str | None) -> str | None:
        if v is not None and not v.strip():
            raise ValueError("Title cannot be empty")
        return v