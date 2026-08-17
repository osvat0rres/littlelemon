from django.shortcuts import render
from .serializer import BookingSerializer, MenuSerializer
from rest_framework import generics
from .models import Booking, Menu
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request,'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    