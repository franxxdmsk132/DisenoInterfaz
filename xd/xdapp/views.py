from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, "xdapp/index.html")
def about (request):
    return render( request, "xdapp/about.html")