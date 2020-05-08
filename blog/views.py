from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    introduction = Blog.objects
    return render(request, 'home.html', {'intro':introduction})