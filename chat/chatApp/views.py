from django.shortcuts import render
from .models import ChatRoom
# Create your views here.
def index(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'index.html', {'rooms' : rooms})

def chat_rooms(request , slug):
    chat = ChatRoom.objects.get(slug=slug)
    return render(request , 'rooms.html' , {"chat" : chat})