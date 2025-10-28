import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

def make_client(token=None):
    c = APIClient()
    if token:
        c.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return c

def signup_and_login(email="a@example.com", password="pass12345"):
    c = make_client()
    r = c.post(reverse('signup'), {"email": email, "password": password}, format='json')
    assert r.status_code == 201
    r = c.post(reverse('login'), {"email": email, "password": password}, format='json')
    assert r.status_code == 200
    return r.data["access"]

def test_user_can_signup_creates_account():
    c = make_client()
    r = c.post(reverse('signup'), {"email": "u1@example.com", "password": "pass12345"}, format='json')
    assert r.status_code == 201
    assert User.objects.filter(username="u1@example.com").exists()

def test_user_can_login_and_logout():
    token = signup_and_login()
    c = make_client(token)
    r = c.post(reverse('logout'), {}, format='json')
    assert r.status_code == 200
    assert r.data["detail"] == "Logged out"

def test_tasks_persist_across_sessions():
    token1 = signup_and_login("p@example.com", "pass12345")
    c1 = make_client(token1)
    r = c1.post("/api/tasks/", {"title": "Finish TDD", "completed": False}, format='json')
    assert r.status_code == 201
    token2 = signup_and_login("p@example.com", "pass12345")
    c2 = make_client(token2)
    r = c2.get("/api/tasks/")
    assert any(t["title"] == "Finish TDD" for t in r.data)

def test_sync_across_devices_same_user():
    tokenA = signup_and_login("sync@example.com", "pass12345")
    tokenB = signup_and_login("sync@example.com", "pass12345")
    a = make_client(tokenA); b = make_client(tokenB)
    a.post("/api/tasks/", {"title": "Shared View", "completed": False}, format='json')
    r = b.get("/api/tasks/")
    assert any(t["title"] == "Shared View" for t in r.data)
