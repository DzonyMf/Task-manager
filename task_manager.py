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
name = input("Name your task ")
details = input("What are the details? ")
while True:
    try:
        importance = int(input("How important is this task on scale 1 to 10? "))
        break
    except ValueError as e:
        print(e, "Insert only number")

created_at = datetime.now()
is_done = False
task1 = Task(name, details, importance, created_at, is_done)
tasks.append(task1)

for task in tasks:
    print(task)




