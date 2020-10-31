from django.urls import path
from .views import CompetitorDetail, LoginView, LogoutView


urlpatterns = [
    path('competitor/<pk>/', CompetitorDetail.as_view(),
         name='competitor_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
