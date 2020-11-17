from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Book, Cart
from .serializers import BookSerializer, CartSerializer, UserSerializer
from django.contrib.auth.models import User


class HelloView(APIView):
    def get(self, request):
        return Response({'Hello': 'world'})


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
