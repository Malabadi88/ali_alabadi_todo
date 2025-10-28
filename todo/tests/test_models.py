import pytest
from django.contrib.auth.models import User
from todo.models import Task

@pytest.mark.django_db
def test_task_creation():
    user = User.objects.create_user(username="modeltest@example.com", password="pass123")
    task = Task.objects.create(user=user, title="Test Task", completed=False)
    assert task.id is not None
    assert task.user == user
    assert task.title == "Test Task"