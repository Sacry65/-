from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def pasta(request):
    return render(request, 'pasta.html')

def salat(request):
    return render(request, 'salat.html')

def soup(request):
    return render(request, 'soup.html')
