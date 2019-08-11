from django.urls import path
from lists import views


urlpatterns = [
    path('<path:list_id>/', views.view_list, name='view_list'),
    path('<path:list_id>/add_item', views.add_item, name='add_item'),
    path('new', views.new_list, name='new_list'),
]