from django.urls import path, include
from .views import ProtectedView,register_user
from rest_framework.routers import DefaultRouter
from .views import CarViewSet,RentalViewSet,PurchaseViewSet,register_user
router = DefaultRouter()
router.register(r'cars',CarViewSet)
router.register(r'rentals',RentalViewSet)
router.register(r'purchases',PurchaseViewSet)

urlpatterns = [
    path('protected/',ProtectedView.as_view(),name='protected'),
    path('',include(router.urls)),
    path('register/',register_user)
]