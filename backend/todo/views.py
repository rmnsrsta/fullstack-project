from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World, This is the index page of todos')

