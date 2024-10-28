from django.shortcuts import render

def beranda(request):
    return render(request, 'beranda.html')

def medsos(request):
    return render(request, 'medsos.html')

def pendidikan(request):
    return render(request, 'pendidikan.html')

def pengalaman(request):
    return render(request, 'pengalaman.html')