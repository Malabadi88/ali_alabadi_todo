from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>ToDo App is running ✅</h1>")

urlpatterns = [
    path('', include('todo.urls')),  # route frontend pages
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),  # API routes
]
