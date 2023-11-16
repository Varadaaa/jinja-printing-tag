from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='its okay u will get a job'
    d={'reality': data}
    return render(request, 'data_render.html', context= d )