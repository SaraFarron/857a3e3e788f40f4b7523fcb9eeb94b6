from django.db import models
from django.utils.translation import ugettext_lazy as _
from .tasks import generate_picture


class Function(models.Model):
    statement = models.CharField(max_length=128, verbose_name='Функция')
    dt = models.IntegerField(verbose_name='Шаг t, часы')
    interval = models.IntegerField(verbose_name='Интервал t, дней')
    graph = models.ImageField(null=True, blank=True, verbose_name='График')
    creation_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата обработки')

    def __str__(self):
        return self.statement

    class Meta:
        verbose_name = _('функцию')
        verbose_name_plural = _('функции')

    def save(self, *args, **kwargs):
        self.image = generate_picture.delay(self.statement, self.dt, self.interval)
        super(Function, self).save(*args, **kwargs)
