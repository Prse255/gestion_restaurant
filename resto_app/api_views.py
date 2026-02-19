from rest_framework import viewsets
from .models import Client, Plat, Commande, DetailCommande
from .serializers import ClientSerializer, PlatSerializer, CommandeSerializer, DetailCommandeSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by("nom")
    serializer_class = ClientSerializer


class PlatViewSet(viewsets.ModelViewSet):
    queryset = Plat.objects.all().order_by("nom")
    serializer_class = PlatSerializer


class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all().order_by("-date_commande")
    serializer_class = CommandeSerializer


class DetailCommandeViewSet(viewsets.ModelViewSet):
    queryset = DetailCommande.objects.all()
    serializer_class = DetailCommandeSerializer
