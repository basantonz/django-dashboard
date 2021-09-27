from django.urls import path
from .views import home,tiendas,fashion,electro,houseful,pets,kid,configuracion,usuarios
from dash.controllers import dashControllers, prueba_controller

urlpatterns = [
    path("", home, name="home"),
    path("prueba/", prueba_controller.obtainAllData),
    path('obtainAllData/', dashControllers.obtainAllData),
    path('tiendas/',tiendas, name='tiendas'),
    path('tiendas/fashion',fashion, name='fashion'),
    path('tiendas/electro',electro, name='electro'),
    path('tiendas/houseful',houseful, name='houseful'),
    path('tiendas/pets',pets, name='pets'),
    path('tiendas/kid',kid,name='kid'),
    path('configuracion/',configuracion,name='configuracion'),
    path('usuarios/',usuarios,name='usuarios'),
]