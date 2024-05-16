# myapp/tasks.py
from celery import shared_task

@shared_task(bind=True)
def my_task(self):
    # Task logic here
    for i in range(20):
        print(i)
    return "Done"


@shared_task(bind=True)
def sample_task(self):
    # Task logic here
    print("task executed successfully")
    return "Done"
