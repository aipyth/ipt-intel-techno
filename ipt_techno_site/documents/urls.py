from django.urls import path

from .views import DocPageDetail, DocPageList


urlpatterns = [
    path('<slug:slug>/', DocPageDetail.as_view(), name='documents_detail'),
    path('', DocPageList.as_view(), name='documents_list'),
]
