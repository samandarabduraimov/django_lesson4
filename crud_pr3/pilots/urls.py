from django.urls import path
from .views import get_info, get_pilots, detail, add_pilots, update_pilots


app_name = 'pilots'
urlpatterns = [
    path('', get_info, name='get_info'),
    path('pilots/<int:pk>', get_pilots, name='get_pilots'),
    path('pilots/detail/<int:pk>', detail, name='detail'),
    path('add_pilots', add_pilots, name='add_pilots'),
    path('update/<int:pk>', update_pilots, name='update'),
]