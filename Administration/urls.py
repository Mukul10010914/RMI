from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('Login/', login, name='login'),
    path('Add Product/', add_product, name='add_product'),
    path('Add Category/', add_cat, name='add_cat'),
    path('add_item/', add_item, name='add_item'),
    path('Home/', ahome, name='ahome'),
    path('View Enqueries/', enqueries, name='enqueries'),
    path('View Reviews/', vreviews, name='vreviews'),
    path('Logout/', logout, name='logout'),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)