from django.urls import path
from market.sellers import views

urlpatterns = [
    # Products
    path("product/create/", views.ProductCreateView.as_view(), name='product-create'),
    path("product/list/", views.ProductListView.as_view(), name='products-list'),
    path("product/<int:pk>/", views.ProductView.as_view(), name='products'),
    # Factories
    path("factory/create/", views.FactoryCreateView.as_view(), name='factory-create'),
    path("factory/list/", views.FactoryListView.as_view(), name='factory-list'),
    path("factory/<int:pk>/", views.FactoryView.as_view(), name='factories'),
    # RetailNetwork
    path("retail_network/create/", views.RetailNetworkCreateView.as_view(), name='retail_network-create'),
    path("retail_network/list/", views.RetailNetworkListView.as_view(), name='retail_network-list'),
    path("retail_network/<int:pk>/", views.RetailNetworkView.as_view(), name='retail_network'),
    # PrivateBusinessman
    path("private_businessman/create/", views.PrivateBusinessmanCreateView.as_view(), name='private_businessman-create'),
    path("private_businessman/list/", views.PrivateBusinessmanListView.as_view(), name='private_businessman-list'),
    path("private_businessman/<int:pk>/", views.PrivateBusinessmanView.as_view(), name='private_businessman'),

]
