from django.shortcuts import render

# Create your views here.

def index(request):
    mydict = {'text': 'This is index page',
              'number' : 100,
              }
    return render(request, 'Basicapp/index.html', mydict)

def other(request):
    return render(request, 'Basicapp/other.html')

def relative_templates(request):
    return render(request, 'Basicapp/relative_templates.html')

def base(request):
    return render(request, 'Basicapp/base.html')