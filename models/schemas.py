from pydantic import BaseModel

class BaseTask(BaseModel):
    title: str
    description: str
    status: str

class CreateTask(BaseTask):
    pass

class Task(BaseTask):
    task_id: int
    project_id: int
