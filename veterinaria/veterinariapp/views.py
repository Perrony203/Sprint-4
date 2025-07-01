from django.shortcuts import render

# Create your views here.
def landingView(request):
    return render(request, 'landing.html')

def inicioView(request):
    return render(request, 'inicio.html')