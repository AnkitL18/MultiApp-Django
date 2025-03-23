from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to App1 Home</h1><a href='/app2/'>Go to App2</a>")
