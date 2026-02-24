from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db
from task_controller import (
    create_task,
    get_tasks,
    get_task_by_id,
    delete_task,
    update_task_status,
    filter_tasks
)
from auth import authenticate_user, create_access_token, get_current_user, create_default_user

# ---------------- INIT APP ---------------- #
models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Student's Task Manager - Advanced by Hamed Werteni")

# ---------------- CREATE DEFAULT USER ---------------- #
# This will create the user HamedMeyo automatically if not exists
with next(get_db()) as db:
    create_default_user(db)


# ---------------- ROOT ---------------- #
@app.get("/")
def root():
    return {"message": "Student’s Task Manager ADVANCED is running — by Hamed Werteni"}


# ---------------- LOGIN ---------------- #
@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(username, password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# ---------------- CREATE TASK ---------------- #
@app.post("/tasks", response_model=schemas.Task)
def add_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    return create_task(db, task, owner=user)


# ---------------- GET ALL TASKS ---------------- #
@app.get("/tasks", response_model=List[schemas.Task])
def read_tasks(
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    return get_tasks(db)


# ---------------- GET TASK BY ID ---------------- #
@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# ---------------- DELETE TASK ---------------- #
@app.delete("/tasks/{task_id}")
def remove_task(
    task_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    task = delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}


# ---------------- PATCH TASK ---------------- #
@app.patch("/tasks/{task_id}", response_model=schemas.Task)
def patch_task(
    task_id: int,
    completed: bool,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    task = update_task_status(db, task_id, completed)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# ---------------- FILTER TASKS ---------------- #
@app.get("/tasks/filter/{status}", response_model=List[schemas.Task])
def filter_task_route(
    status: str,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    if status.lower() not in ["completed", "pending"]:
        raise HTTPException(status_code=400, detail="Invalid filter status")
    return filter_tasks(db, status.lower())