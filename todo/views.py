from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItems

# Create your views here.

def myTodo(request):
	all_todo_itmes = TodoItems.objects.all()


	return render(request, 'todo.html', {'all_items': all_todo_itmes})


def addTodo(request):
	# create a new todo all_items then save it then return to called url
	new_item = TodoItems(content = request.POST['content'])
	new_item.save()

	return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
	TodoItems.objects.get(id = todo_id).delete()

	return HttpResponseRedirect('/todo/')


