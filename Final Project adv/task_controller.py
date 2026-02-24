from sqlalchemy.orm import Session
import models
import schemas


# ---------------- CREATE TASK ---------------- #
def create_task(db: Session, task: schemas.TaskCreate, owner=None):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        completed=False,
        owner_id=owner.id if owner else 1  # Default owner_id = 1 if not provided
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# ---------------- GET ALL TASKS ---------------- #
def get_tasks(db: Session):
    return db.query(models.Task).all()


# ---------------- GET TASK BY ID ---------------- #
def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


# ---------------- DELETE TASK ---------------- #
def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task


# ---------------- UPDATE TASK STATUS (PATCH) ---------------- #
def update_task_status(db: Session, task_id: int, completed: bool):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None
    task.completed = completed
    db.commit()
    db.refresh(task)
    return task


# ---------------- FILTER TASKS ---------------- #
def filter_tasks(db: Session, status: str):
    if status == "completed":
        return db.query(models.Task).filter(models.Task.completed == True).all()
    elif status == "pending":
        return db.query(models.Task).filter(models.Task.completed == False).all()
    else:
        return []