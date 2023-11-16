from django.shortcuts import render

# Create your views here.
def data(request):
    inf='This shall to pass'
    d={'hope': inf}
    return render(request, 'data.html', context=d)