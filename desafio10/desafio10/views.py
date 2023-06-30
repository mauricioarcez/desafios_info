from django.shortcuts import render

def index(request):
    
    template_name = 'index.html'
    nombres = ['mauri','leo','nai']
    contexto = {'nombres': nombres}    
    
    return render(request,template_name,contexto)

