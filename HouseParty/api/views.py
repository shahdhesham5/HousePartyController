from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
# Create your views here.
def main(request):
    return HttpResponse("Hello")
#Using generics create function to allow us create a room instance from the api 
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
#Using generics List function to only retrieve the data as a list
class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer