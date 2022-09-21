from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def hw(request):
    return render(request, "homework.html")

def HttpResponse(request):
    return render(request, "response.html")
# Create your views here.
