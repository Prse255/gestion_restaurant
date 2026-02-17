from django.contrib import admin
from .models import Client, Plat, Commande, DetailCommande


# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'telephone')
    search_fields = ('nom', 'telephone')
    ordering = ('nom',)



@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prix', 'disponible')
    list_filter = ('disponible',)
    search_fields = ('nom',)
    ordering = ('nom',)



class DetailCommandeInline(admin.TabularInline):
    model = DetailCommande
    extra = 1
    autocomplete_fields = ('plat',)


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_commande')
    list_filter = ('date_commande',)
    search_fields = ('client__nom',)
    ordering = ('-date_commande',)
    autocomplete_fields = ('client',)
    inlines = [DetailCommandeInline]


@admin.register(DetailCommande)
class DetailCommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'commande', 'plat', 'quantite')
    list_filter = ('plat',)
    search_fields = ('plat__nom',)

