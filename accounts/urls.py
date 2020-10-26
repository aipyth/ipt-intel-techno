from django.urls import path
from .views import CompetitorDetail


urlpatterns = [
    path('competitor/<pk>/', CompetitorDetail.as_view(),
         name='competitor_detail'),
]
