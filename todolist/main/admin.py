from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Tasks, Tables
# Register your models here.


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    pass

@admin.register(Tables)
class TablesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("category", )}