from django.shortcuts import render

# Create your views here.
def hoja_vida(request):
    return render(request, 'hoja-vida-dev2.html')
