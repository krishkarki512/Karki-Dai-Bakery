from django.urls import path
from .views import home, search_cakes


urlpatterns = [
    path('', home, name='home'),
    path('search/', search_cakes, name='search'),
]
