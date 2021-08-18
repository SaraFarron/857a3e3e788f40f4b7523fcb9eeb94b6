from celery import shared_task
from .models import Function


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def generate_picture():
    pass

# чтобы селери делал то что написано в таске надо добавить к команде --pool=solo
