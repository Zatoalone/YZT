from django.urls import path
from . import views

app_name = 'well'
urlpatterns = [
    path('', views.WellView.as_view(), name='wells'),
    path('w/<slug:well>/', views.WellDetailView.as_view(), name='well_detail'),
    path('wb/<slug:wellbore>/', views.WellboreDetailView.as_view(), name='wellbore'),
]
