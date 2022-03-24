from django.urls import path

from . import views

urlpatterns = [
    path('',views.topmenu, name="topmenu"),
]