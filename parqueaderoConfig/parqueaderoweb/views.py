from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'index.html')
def conductor(request):
    return render (request,'conductor.html')

def registro(request):
    return render (request,'registroTicket.html')
    
