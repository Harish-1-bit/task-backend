from fastapi import APIRouter, Depends, status
from src.Task import controller
from src.Task.dtos import TaskSchema
from src.utils.db import get_db
from src.utils.authenticateUser import get_current_user

task_route = APIRouter(prefix='/task',
                       dependencies=[Depends(get_current_user)]
                       )

@task_route.post('/', status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db = Depends(get_db)):
    return controller.create_task(body, db)

@task_route.get('/',status_code=status.HTTP_200_OK)
def get_task(db = Depends(get_db)):
    return controller.get_task(db)

@task_route.get('/{id}',status_code=status.HTTP_200_OK)
def get_one_task(id, db = Depends(get_db)):
    return controller.get_one_task(id,db)

@task_route.patch('/{id}',status_code=status.HTTP_201_CREATED)
def update_task(body : TaskSchema ,id :int , db = Depends(get_db)):
    return controller.update_task(body, id, db)

@task_route.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id : int, db=Depends(get_db)):
    return controller.delete_task(id,db)