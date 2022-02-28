from django.urls import path
from . import views

urlpatterns = [
    path('oils/', views.OilsList.as_view(), name='oils_list'),
    path('oils/<int:pk>', views.OilsDetail.as_view(), name='oils_detail')
]