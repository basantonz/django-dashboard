from django.urls import path
from .views import home,tiendas,fashion,electro,househome,beautyhealth,kids,configuracion,usuarios
from dash.controllers import dashControllers, prueba_controller

urlpatterns = [
    path("", home, name="home"),
    path("prueba/", prueba_controller.obtainAllData),
    path('obtainAllData/', dashControllers.obtainAllData),
    path('tiendas/',tiendas, name='tiendas'),
    path('tiendas/fashion',fashion, name='fashion'),
    path('tiendas/electro',electro, name='electro'),
    path('tiendas/househome',househome, name='househome'),
    path('tiendas/beautyhealth',beautyhealth, name='beautyhealth'),
    path('configuracion/',configuracion,name='configuracion'),
    path('usuarios/',usuarios,name='usuarios'),
]