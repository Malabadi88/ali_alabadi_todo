from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('add/', views.add_todo, name='add-todo'),
    path('complete/<int:item_id>/', views.complete_todo, name='complete-todo'),
    path('delete/<int:item_id>/', views.delete_todo, name='delete-todo'),
]
