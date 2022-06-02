from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'index.html')

def registro(request):
    return render (request,'registroTicket.html')
    
