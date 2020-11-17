from django.urls import path, include
from .views import HelloView, BookViewSet, CartViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('cart', CartViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', HelloView.as_view())
]
