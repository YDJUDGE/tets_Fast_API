from .schemas import CreateTask, Task
from dataclasses import dataclass, field

@dataclass
class Task_Storage:
    last_task_id: int = 0
    last_project_id: int = 0
    tasks: dict[int: Task] = field(default_factory=dict)

    @property
    def next_task_id(self):
        self.last_task_id += 1
        return self.last_task_id

    @property
    def next_project_id(self):
        self.last_project_id += 1
        return self.last_project_id


    def create_t(self, task: CreateTask):
        task_id = self.next_task_id
        project_id = self.next_project_id
        new_task = Task(task_id=task_id, project_id=project_id, **task.dict())
        self.tasks[task_id] = new_task
        return new_task

    def get_tasks(self):
        return list(self.tasks.values())

    def get_task_by_id(self, id:int):
        return self.tasks.get(id, None)

    def delete_task_by_id(self, id:int):
        return self.tasks.pop(id, None)

    def update_task_by_id(self, id: int, updated_task: CreateTask):
        if id in self.tasks:
            for key, value in updated_task.dict().items():
                setattr(self.tasks[id], key, value)
            return self.tasks[id]
        return None

task_storage = Task_Storage()




