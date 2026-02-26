from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Client, Plat, Commande, DetailCommande
from .serializers import ClientSerializer, PlatSerializer, CommandeSerializer, DetailCommandeSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by("nom")
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["nom", "telephone"]
    ordering_fields = ["id", "nom"]

    # filtres avancés (iexact, icontains) comme dans le cours
    filterset_fields = {
        "nom": ["iexact", "icontains"],
        "telephone": ["iexact", "icontains"],
    }


class PlatViewSet(viewsets.ModelViewSet):
    queryset = Plat.objects.all().order_by("nom")
    serializer_class = PlatSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["nom"]
    ordering_fields = ["id", "nom", "prix", "disponible"]

    filterset_fields = {
        "nom": ["iexact", "icontains"],
        "prix": ["gte", "lte"],
        "disponible": ["exact"],
    }


class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all().order_by("-date_commande")
    serializer_class = CommandeSerializer
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["client__nom", "statut"]
    ordering_fields = ["id", "date_commande", "statut", "client"]

    filterset_fields = {
        "statut": ["exact"],
        "client": ["exact"],
        "date_commande": ["gte", "lte"],
    }


class DetailCommandeViewSet(viewsets.ModelViewSet):
    queryset = DetailCommande.objects.all().order_by("id")
    serializer_class = DetailCommandeSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ["id", "quantite"]

    filterset_fields = {
        "commande": ["exact"],
        "plat": ["exact"],
        "quantite": ["gte", "lte"],
    }