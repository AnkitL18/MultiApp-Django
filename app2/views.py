from django.http import HttpResponse

def sample(request):
    return HttpResponse("<h1>This is App2 Sample Page</h1><a href='/'>Go to Home</a>")
