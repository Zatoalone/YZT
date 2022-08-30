from django.urls import path
from . import views

app_name = 'rig'
urlpatterns = [
    path('', views.RigView.as_view(), name='rigss'),
    path('<slug:rig>/', views.RigDetailView.as_view(), name='rig_detail'),
]
