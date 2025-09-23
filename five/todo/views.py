from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    """
    Handles displaying the list of to-do items.
    """
    items = TodoItem.objects.all()
    return render(request, 'todo/todo.html', {'items': items})

def add_todo(request):
    """
    Handles adding a new to-do item.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TodoItem.objects.create(title=title)
    return redirect('todo-list')

def complete_todo(request, item_id):
    """
    Marks a to-do item as completed.
    """
    item = TodoItem.objects.get(id=item_id)
    item.completed = True
    item.save()
    return redirect('todo-list')

def delete_todo(request, item_id):
    """
    Deletes a to-do item.
    """
    TodoItem.objects.get(id=item_id).delete()
    return redirect('todo-list')
