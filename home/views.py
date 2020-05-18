from django.shortcuts import render

def home(request):
	return render(request, 'home.html')
def pudge(request):
	return render(request, 'pudge.html')
