from django.urls import path
from .views import addshow, delete, modify

urlpatterns = [
    path('', addshow, name='addshow'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('modify/<int:pk>/', modify, name='modify'),  
]
