from django.shortcuts import render

# Create your views here.

def personalIndex(request):
	return render(request, 'personal/home.html')