from fastapi import APIRouter, status, HTTPException, Response
from models.crud import  task_storage
from models.schemas import Task, CreateTask

router = APIRouter()

@router.post("/create_task", response_model=Task)
def create_t(task: CreateTask):
    res_create = task_storage.create_t(task)
    if res_create:
        return res_create
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/get_tasks", response_model=list[Task])
def get_tasks():
    res_get = task_storage.get_tasks()
    if res_get:
        return res_get
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/{id}", response_model=Task)
def get_task_by_id(id: int):
    res = task_storage.get_task_by_id(id=id)
    if res:
        return res
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/delete/{id}", response_model=Task)
def delete_task_by_id(id: int):
    res_delete = task_storage.delete_task_by_id(id)
    if res_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=Task)
def update_task_by_id(id: int, task: CreateTask):
    res_update = task_storage.update_task_by_id(id, task)
    if res_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return res_update

