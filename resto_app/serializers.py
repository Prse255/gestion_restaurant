from rest_framework import serializers
from .models import Client, Plat, Commande, DetailCommande


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = "__all__"


class DetailCommandeSerializer(serializers.ModelSerializer):
    plat_nom = serializers.CharField(source="plat.nom", read_only=True)
    plat_prix = serializers.DecimalField(source="plat.prix", max_digits=8, decimal_places=2, read_only=True)

    class Meta:
        model = DetailCommande
        fields = ["id", "commande", "plat", "plat_nom", "plat_prix", "quantite"]


class CommandeSerializer(serializers.ModelSerializer):
    client_nom = serializers.CharField(source="client.nom", read_only=True)
    details = DetailCommandeSerializer(source="detailcommande_set", many=True, read_only=True)

    class Meta:
        model = Commande
        fields = ["id", "client", "client_nom", "date_commande", "statut", "details"]
