from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.dependencies import get_current_user
from app.dtos.requests import TaskCreateRequest, TaskUpdateRequest
from app.dtos.responses import TaskResponse
from app.enums import Priority, Role, Status
from app.models import Task, User

router = APIRouter(prefix="/tasks", tags=["tasks"])


def get_task_or_404(task_id: int, session: Session, current_user: User) -> Task:
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if current_user.role != Role.admin and task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("", response_model=TaskResponse, status_code=201)
def create_task(
    task_data: TaskCreateRequest,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = Task(
        title=task_data.title,
        priority=task_data.priority,
        due_date=task_data.due_date,
        user_id=current_user.id,
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.get("", response_model=list[TaskResponse])
def list_tasks(
    status_filter: Status | None = None,
    priority_filter: Priority | None = None,
    skip: int = 0,
    limit: int = 20,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    query = select(Task)

    if current_user.role != Role.admin:
        query = query.where(Task.user_id == current_user.id)

    if status_filter is not None:
        query = query.where(Task.status == status_filter)

    if priority_filter is not None:
        query = query.where(Task.priority == priority_filter)

    query = query.offset(skip).limit(limit)
    return session.exec(query).all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return get_task_or_404(task_id, session, current_user)


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdateRequest,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = get_task_or_404(task_id, session, current_user)
    update_fields = task_data.model_dump(exclude_unset=True)
    for field, value in update_fields.items():
        setattr(task, field, value)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(
    task_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = get_task_or_404(task_id, session, current_user)
    if task.status == Status.done:
        raise HTTPException(status_code=400, detail="Task is already done")
    task.status = Status.done
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.delete("/{task_id}", status_code=204)
def delete_task(
    task_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = get_task_or_404(task_id, session, current_user)
    session.delete(task)
    session.commit()