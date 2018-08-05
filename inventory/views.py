from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# CRUD operations for Items


class ItemCreateView(CreateView):
    model = Item
    fields = "__all__"
    template_name = "inventory/item_create.html"

    def get_success_url(self):
        return reversed("None")


class ItemListView(ListView):
    model = Item
    queryset = Item.objects.all()
    fields = "__all__"
    template_name = "inventory/item_list.html"

    def get_success_url(self):
        return reversed("item_list")


class ItemUpdateView(UpdateView):
    model = Item
    fields = "__all__"
    template_name = "inventory/item_update.html"

    def get_success_url(self):
        return reversed("item_list")


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "inventory/item_delete.html"

    def get_success_url(self):
        return reversed("item_list")


# CRUD operations for Houses

class HouseCreateView(CreateView):
    model = House
    fields = "__all__"
    template_name = "inventory/house_create.html"


def get_success_url(self):
    return reversed("house_list")


class HouseListView(ListView):
    model = House
    queryset = House.objects.all()
    fields = "__all__"
    template_name = "inventory/house_list.html"

    def get_success_url(self):
        return reversed("house_list")


class HouseUpdateView(UpdateView):
    model = House
    fields = "__all__"
    template_name = "inventory/house_update.html"

    def get_success_url(self):
        return reversed("house_list")


class HouseDeleteView(DeleteView):
    model = House
    template_name = "inventory/house_delete.html"

    def get_success_url(self):
        return reversed("house_list")



# CRUD operations for Buildings

class BuildingCreateView(CreateView):
    model = Building
    fields = "__all__"
    template_name = "inventory/building_create.html"


def get_success_url(self):
    return reversed("building_list")


class BuildingListView(ListView):
    model = Building
    queryset = Building.objects.all()
    fields = "__all__"
    template_name = "inventory/building_list.html"

    def get_success_url(self):
        return reversed("building_list")


class BuildingUpdateView(UpdateView):
    model = Building
    fields = "__all__"
    template_name = "inventory/building_update.html"

    def get_success_url(self):
        return reversed("building_list")


class BuildingDeleteView(DeleteView):
    model = Building
    template_name = "inventory/building_delete.html"

    def get_success_url(self):
        return reversed("building_list")


