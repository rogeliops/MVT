from django.urls import path

from MyApp.views import mostrar_familia

urlpatterns = [
    path('', mostrar_familia)
]