from celery import shared_task
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import re
from datetime import datetime
from time import sleep
from django.core.files.images import ImageFile
from .models import Function


replacements = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

allowed_words = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
]


def string2func(string):
    """ Из строки делает выражение для функции """

    for word in re.findall('[a-zA-Z_]+', string):
        if word not in allowed_words:
            raise ValueError(
                f'{word} is forbidden to use in math expression'
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    def func(x):
        return eval(string)

    return func


@shared_task()
def generate_picture(statement, dt, interval, func_id):
    x = np.linspace(datetime.now().day - interval, datetime.now().day, num=dt*interval)
    y = [string2func(statement)(t) for t in x]
    plt.plot(x, y)
    image = BytesIO()
    plt.savefig(image, format='png')
    picture = ImageFile(image)
    while not Function.objects.filter(id=func_id):
        sleep(1)
        print(f'id = {func_id}, dt = {dt}, statement = {statement}, interval = {interval}')
    else:
        Function.objects.get(id=func_id).update(graph=picture)


# чтобы селери делал то что написано в таске надо добавить к команде --pool=solo
