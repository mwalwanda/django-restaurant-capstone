from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .permissions import IsAuthenticatedUser

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
   
        
# Similarly, you can create views for Booking model if needed
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 
 