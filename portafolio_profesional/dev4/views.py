from django.shortcuts import render

def hoja_de_vida(request):
    # Cambiamos "index.html" por "hoja4.html"
    return render(request, "hoja4.html")