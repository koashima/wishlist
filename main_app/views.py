from django.shortcuts import render
from . models import Item
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView


class WishList(ListView):
    model = Item

class WishCreate(CreateView):
    model = Item
    fields = '__all__'

class WishDelete(DeleteView):
    model = Item
    success_url = '/'
