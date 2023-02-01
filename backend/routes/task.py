from config.db import Session
from fastapi import APIRouter, Response, Path, HTTPException, status
from models.models import Task
from schemas.schema import TaskSchema

task = APIRouter(prefix="/api")
session = Session()

@task.post("/add")
async def createTask(data: TaskSchema):
    if not data.name:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Task name is required")
    task = Task(data.name)
    session.add(task)
    try:
        session.commit()
    except:
        session.rollback()
    session.close()
    return Response(content="Task created successfully!", status_code=status.HTTP_201_CREATED)

@task.get("/all")
async def getAllTasks():
    return session.query(Task).all()

@task.post('/update/{id}')
async def updateTask(id: int, data: TaskSchema):
    if not data.name:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Task name is required")
    session.query(Task).filter(Task.id == id).update({'name': data.name})
    try:
        session.commit()
    except:
        session.rollback()
    session.close()
    return Response(content="Task updated successfully", status_code=status.HTTP_200_OK)

@task.get("/change-task-status/{id}")
async def changeTaskStatus(id: int):
    task = session.query(Task).filter(Task.id == id).first()
    session.query(Task).filter(Task.id == id).update({'complete': not task.complete})
    session.commit()
    session.close()
    return Response(content="Task updated successfully", status_code=status.HTTP_200_OK)

@task.delete('/delete/{id}')
async def deleteTask(id: int):
    session.query(Task).filter(Task.id == id).delete()
    session.commit()
    session.close()
    return Response(content="Task deleted successfully", status_code=status.HTTP_200_OK)