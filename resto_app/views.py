from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from .models import Client, Plat, Commande, DetailCommande
from .forms import ClientForm, PlatForm, CommandeForm, DetailCommandeFormSet
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator



# ----------------------------
# COMMANDES (Accueil + CRUD)
# ----------------------------
@method_decorator(login_required, name="dispatch")
@method_decorator(permission_required("resto_app.view_commande", raise_exception=True), name="dispatch")
class CommandeListView(ListView):
    model = Commande
    template_name = "resto_app/commandes/list.html"
    context_object_name = "commandes"
    ordering = ["-date_commande"]

    def get_queryset(self):
        return super().get_queryset().select_related("client")

@login_required
@permission_required("resto_app.add_commande", raise_exception=True)
def commande_create(request):
    if request.method == "POST":
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save()
            formset = DetailCommandeFormSet(request.POST, instance=commande)

            if formset.is_valid():
                formset.save()
                return redirect("commande_detail", pk=commande.pk)

            # éviter une commande vide si le formset est invalide
            commande.delete()
        else:
            formset = DetailCommandeFormSet(request.POST)
    else:
        form = CommandeForm()
        formset = DetailCommandeFormSet()

    return render(request, "resto_app/commandes/form.html", {
        "title": "Nouvelle commande",
        "form": form,
        "formset": formset,
    })

@login_required
@permission_required("resto_app.change_commande", raise_exception=True)
def commande_update(request, pk):
    commande = get_object_or_404(Commande, pk=pk)

    if request.method == "POST":
        form = CommandeForm(request.POST, instance=commande)
        formset = DetailCommandeFormSet(request.POST, instance=commande)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("commande_detail", pk=commande.pk)
    else:
        form = CommandeForm(instance=commande)
        formset = DetailCommandeFormSet(instance=commande)

    return render(request, "resto_app/commandes/form.html", {
        "title": f"Modifier commande #{commande.id}",
        "form": form,
        "formset": formset,
        "commande": commande,
    })

@login_required
@permission_required("resto_app.view_commande", raise_exception=True)
def commande_detail(request, pk):
    commande = get_object_or_404(Commande.objects.select_related("client"), pk=pk)
    details = DetailCommande.objects.filter(commande=commande).select_related("plat")

    total = 0
    for d in details:
        if d.plat is not None:
            total += float(d.plat.prix) * d.quantite

    return render(request, "resto_app/commandes/detail.html", {
        "commande": commande,
        "details": details,
        "total": total,
    })

@method_decorator(login_required, name="dispatch")
@method_decorator(permission_required("resto_app.delete_commande", raise_exception=True), name="dispatch")
class CommandeDeleteView(DeleteView):
    model = Commande
    template_name = "resto_app/generic/confirm_delete.html"
    success_url = reverse_lazy("commande_list")


# ----------------------------
# CLIENTS (1 page : liste + ajout rapide)
# ----------------------------

def client_list(request):
    clients = Client.objects.all().order_by("nom")

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm()

    return render(request, "resto_app/clients/list.html", {
        "clients": clients,
        "form": form,
    })


def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_list")
    else:
        form = ClientForm(instance=client)

    # on réutilise la page clients/list en mode "édition"
    clients = Client.objects.all().order_by("nom")
    return render(request, "resto_app/clients/list.html", {
        "clients": clients,
        "form": form,
        "editing": True,
        "edit_id": client.id,
    })


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "resto_app/generic/confirm_delete.html"
    success_url = reverse_lazy("client_list")


# ----------------------------
# PLATS (1 page : liste + ajout rapide)
# ----------------------------

def plat_list(request):
    plats = Plat.objects.all().order_by("nom")

    if request.method == "POST":
        form = PlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plat_list")
    else:
        form = PlatForm()

    return render(request, "resto_app/plats/list.html", {
        "plats": plats,
        "form": form,
    })


def plat_edit(request, pk):
    plat = get_object_or_404(Plat, pk=pk)

    if request.method == "POST":
        form = PlatForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect("plat_list")
    else:
        form = PlatForm(instance=plat)

    plats = Plat.objects.all().order_by("nom")
    return render(request, "resto_app/plats/list.html", {
        "plats": plats,
        "form": form,
        "editing": True,
        "edit_id": plat.id,
    })


class PlatDeleteView(DeleteView):
    model = Plat
    template_name = "resto_app/generic/confirm_delete.html"
    success_url = reverse_lazy("plat_list")
