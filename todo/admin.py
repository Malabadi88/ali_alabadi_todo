from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "user", "created_at")
    search_fields = ("title",)
    list_filter = ("completed",)
