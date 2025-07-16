from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets,permissions
from .models import Car,Rental,Purchase
from .serializers import CarSerializer,RentalSerializer,PurchaseSerializer

# Create your views here.

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username and password:
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created successfully '}, status=201)
    return Response({'error':'Invalid Data'}, status=400)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({"message":f"Welcome, {request.user.username}!"})
    
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

