from django.urls import path

from .views import DocPageDetail


urlpatterns = [
    path('<slug:slug>/', DocPageDetail.as_view(), name='documents-detail'),
]
