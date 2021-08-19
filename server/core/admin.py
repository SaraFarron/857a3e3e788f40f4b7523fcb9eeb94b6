from django.contrib import admin
from .models import Function


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('statement', 'graph', 'interval', 'dt', 'creation_date')
