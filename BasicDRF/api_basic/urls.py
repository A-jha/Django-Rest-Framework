from django.urls import path
from .views import artical_list, artical_detail
urlpatterns = [
    path('', artical_list),
    path('details/<int:pk>/', artical_detail)
]
