from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Plat(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    STATUT_CHOICES = [
        ("EN_ATTENTE", "En attente"),
        ("EN_PREPARATION", "En préparation"),
        ("PRETE", "Prête"),
        ("REMISE", "Remise"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="EN_ATTENTE")

    def __str__(self):
        return f"Commande #{self.id} - {self.client.nom}"



class DetailCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.SET_NULL, null=True, blank=True)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        plat_nom = self.plat.nom if self.plat else "Plat supprimé"
        return f"{plat_nom} x{self.quantite} (Commande #{self.commande.id})"


