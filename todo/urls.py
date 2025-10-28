from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, SignupView, LoginView, LogoutView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/login/',  LoginView.as_view(),  name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]
