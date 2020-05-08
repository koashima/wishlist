from django.shortcuts import render
from . models import Item
from django.views.generic import ListView

class WishList(ListView):
    model = Item


