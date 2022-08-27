from django.shortcuts import render

def question(request):
    return render(request, 'core/teste.html')