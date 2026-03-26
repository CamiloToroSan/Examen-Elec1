from django.shortcuts import render

def hoja_vida(request):
    return render(request, 'dev1/hoja_vida.html')