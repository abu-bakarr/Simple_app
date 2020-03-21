from django.urls import path
from . import views

app_name = 'simple_app'

urlpatterns = [
    path("", views.home, name='home'),
    path("new-search/", views.search, name='search')
]
