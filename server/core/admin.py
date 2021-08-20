from django.contrib import admin
from .models import Function


@admin.action(description='Обновить')
def update_functions(modeladmin, request, queryset):
    queryset.update()


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('statement', 'graph', 'interval', 'dt', 'creation_date')
    actions = [update_functions]
