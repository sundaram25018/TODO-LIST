from sqlalchemy.orm import Session
from main import SessionLocal, TaskModel

db: Session = SessionLocal()

tasks = db.query(TaskModel).all()

for task in tasks:
    print(task.id, task.title, task.description, task.completed)
