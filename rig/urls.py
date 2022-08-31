from django.urls import path
from . import views

app_name = 'rig'
urlpatterns = [
    path('', views.RigView.as_view(), name='rigs'),
    path('<slug:rig>/', views.RigDetailView.as_view(), name='rig_detail'),
]
