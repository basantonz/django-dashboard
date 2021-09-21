from django.urls import path
from .views import home,graficos
from dash.controllers import dashControllers, prueba_controller

urlpatterns = [
    path("", home, name="home"),
    path("prueba/", prueba_controller.obtainAllData),
    path('obtainAllData/', dashControllers.obtainAllData),
    path('graficos/',graficos, name='graficos'),
]
