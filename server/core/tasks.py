from celery import shared_task
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import re
from datetime import datetime


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
def generate_picture(statement, dt, interval):
    x = np.linspace(datetime.now() - interval, datetime.now().day, num=dt*interval)
    y = [string2func(statement)(t) for t in x]
    plt.plot(x, y)
    image = StringIO()
    plt.savefig(image)
    return image

# чтобы селери делал то что написано в таске надо добавить к команде --pool=solo
