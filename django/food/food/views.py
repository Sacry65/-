from django.shortcuts import render

def pasta_view(request):
    return render(request, 'pasta.html')

def salat_view(request):
    return render(request, 'salat.html')

def soup_view(request):
    return render(request, 'soup.html')