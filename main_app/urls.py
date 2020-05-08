from django.urls import path
from . import views 


urlpatterns = [
    path('', views.WishList.as_view(), name='wishlist_index'),
    path('create/', views.WishCreate.as_view(), name='wish_create'),
    path('<int:pk>/delete/', views.WishDelete.as_view(), name='wish_delete')
]