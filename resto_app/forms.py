from django import forms
from django.forms import inlineformset_factory
from .models import Client, Plat, Commande, DetailCommande


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["nom", "telephone"]


class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ["nom", "prix", "disponible"]


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ["client"]


DetailCommandeFormSet = inlineformset_factory(
    Commande,
    DetailCommande,
    fields=["plat", "quantite"],
    extra=5,
    can_delete=True
)
