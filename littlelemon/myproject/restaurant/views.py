from django.shortcuts import render
from .serializer import BookingSerializer, MenuSerializer
from rest_framework import generics
from .models import Booking, Menu
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request,'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})

    
    