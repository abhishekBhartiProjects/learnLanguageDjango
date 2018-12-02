"""learnLanguageProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello.views import myView
from todo.views import myTodo, addTodo, deleteTodo
from personal.views import personalIndex, contact
from blog.views import blog
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', myView),
    path('todo/', myTodo),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('', personalIndex),
    path('contact/', contact),
    # path('blog/', blog),
    path('blog/', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                    template_name="blog/blog.html")),
    path('blog/<slug:pk>/', DetailView.as_view(model=Post, template_name="blog/post.html")),


]
