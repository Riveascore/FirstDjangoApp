from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  context_dict = {
    'insert_me': "Instance variables!!!"
  }
  # return HttpResponse("<h1>Hello World</h1>")
  return render(request, 'first_app/index.html', context=context_dict)
