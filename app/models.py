from datetime import datetime

from sqlmodel import Field, SQLModel

from app.enums import Priority, Status, Role


class User(SQLModel, table=True):
    __table_args__ = {"sqlite_autoincrement": True}

    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    hashed_password: str
    role: Role = Role.user
    is_active: bool = True


class Task(SQLModel, table=True):
    __table_args__ = {"sqlite_autoincrement": True}

    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
    priority: Priority = Priority.medium
    status: Status = Status.todo
    due_date: datetime | None = None
    date_created: datetime = Field(default_factory=datetime.utcnow)
    user_id: int = Field(foreign_key="user.id")