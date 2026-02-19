from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ClientViewSet, PlatViewSet, CommandeViewSet, DetailCommandeViewSet

router = DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"plats", PlatViewSet)
router.register(r"commandes", CommandeViewSet)
router.register(r"details", DetailCommandeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
