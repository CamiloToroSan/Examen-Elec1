from django.shortcuts import render

# Create your views here.
def hoja_de_vida(request):
    return render(request, "index.html")