from django.shortcuts import render

# Create your views here.

def personalIndex(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/contact.html', {'content': ['If you want to contact me, just email me at ', 'abhishekbharti.inbox@gmail.com']})
