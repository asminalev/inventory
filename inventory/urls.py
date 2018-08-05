from django.conf.urls import url
from inventory import views


urlpatterns = [
    url(r'^item_create/', views.ItemCreateView.as_view(), name='item_create'),
    url(r'^item_list/',views.ItemListView.as_view(), name='item_list'),
    url(r'^item_update/(?P<pk>\d+)/$', views.ItemUpdateView.as_view(), name='item_update'),
    url(r'^item_delete/(?P<pk>\d+)/$', views.ItemDeleteView.as_view(), name='item_delete'),
    url(r'^house_create/', views.HouseCreateView.as_view(), name='house_create'),
    url(r'^house_list/',views.HouseListView.as_view(), name='house_list'),
    url(r'^house_update/(?P<pk>\d+)/$', views.HouseUpdateView.as_view(), name='house_update'),
    url(r'^house_delete/(?P<pk>\d+)/$', views.HouseDeleteView.as_view(), name='house_delete'),
    url(r'^building_create/', views.BuildingCreateView.as_view(), name='building_create'),
    url(r'^building_list/',views.BuildingListView.as_view(), name='building_list'),
    url(r'^building_update/(?P<pk>\d+)/$', views.BuildingUpdateView.as_view(), name='building_update'),
    url(r'^building_delete/(?P<pk>\d+)/$', views.BuildingDeleteView.as_view(), name='building_delete'),

]
