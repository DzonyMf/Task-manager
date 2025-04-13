from datetime import datetime
#Class creating
class Task:
    #Constructor
    def __init__(self, name: str, details: str, importance: int, created_at: datetime, is_done: bool) -> None:
        self.name = name
        self.details = details
        self.importance = importance
        self.created_at = created_at
        self.is_done = is_done
    #Methods
    def __str__(self):
        return f'{self.name}, {self.details}, {self.importance}, {self.created_at}, {self.is_done}'

tasks = []

task1 = Task(input("Name your task "), input("What are the details? "), int(input("How important is this task on scale 1 to 10? ")), datetime.now(), False)
tasks.append(task1)

for task in tasks:
    print(task)




