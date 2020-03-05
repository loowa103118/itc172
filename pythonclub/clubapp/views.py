from django.shortcuts import render
from .models import Meeting



# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getmeetings(request):
     type_list=Meeting.objects.all() 
     return render(request, 'clubapp/meeting.html', {'type_list': type_list})   

    
