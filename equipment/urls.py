from django.urls import path
from . import views

app_name = 'equipment'
urlpatterns = [
    path('', views.EquipmentView.as_view(), name='equipments'),
    path('<slug:equipment>/', views.EquipmentDetailView.as_view(), name='equipment_detail'),
]
