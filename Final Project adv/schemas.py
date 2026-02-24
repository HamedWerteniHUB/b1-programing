from pydantic import BaseModel
from typing import Optional


# ---------------- USER SCHEMAS ---------------- #
class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# ---------------- TASK SCHEMAS ---------------- #
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    completed: Optional[bool] = None
    title: Optional[str] = None
    description: Optional[str] = None


class Task(TaskBase):
    id: int
    completed: bool
    owner_id: int

    class Config:
        orm_mode = True