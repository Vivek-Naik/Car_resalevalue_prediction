from django.urls import path
from . import views
app_name ='sell'

urlpatterns = [
    path('selll/', views.selll, name='selll'),
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),
    
]
