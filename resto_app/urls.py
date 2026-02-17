from django.urls import path
from . import views

urlpatterns = [
    path("", views.CommandeListView.as_view(), name="commande_list"),

    path("commandes/new/", views.commande_create, name="commande_create"),
    path("commandes/<int:pk>/", views.commande_detail, name="commande_detail"),
    path("commandes/<int:pk>/edit/", views.commande_update, name="commande_edit"),
    path("commandes/<int:pk>/delete/", views.CommandeDeleteView.as_view(), name="commande_delete"),

    path("clients/", views.client_list, name="client_list"),
    path("clients/<int:pk>/edit/", views.client_edit, name="client_edit"),
    path("clients/<int:pk>/delete/", views.ClientDeleteView.as_view(), name="client_delete"),

    path("plats/", views.plat_list, name="plat_list"),
    path("plats/<int:pk>/edit/", views.plat_edit, name="plat_edit"),
    path("plats/<int:pk>/delete/", views.PlatDeleteView.as_view(), name="plat_delete"),
]
