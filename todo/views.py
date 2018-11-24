from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myTodo(request):
	return HttpResponse("This is todo app")
