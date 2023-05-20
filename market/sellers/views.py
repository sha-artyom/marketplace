from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from market.sellers.models import Product, Factory, RetailNetwork, PrivateBusinessman
from market.sellers.permissions import ActiveUsers
from market.sellers.serializers import ProductListSerializer, ProductCreateSerializer, ProductSerializer, \
    FactoryListSerializer, FactoryCreateSerializer, FactorySerializer, PrivateBusinessmanSerializer, \
    PrivateBusinessmanCreateSerializer, PrivateBusinessmanListSerializer, RetailNetworkSerializer, \
    RetailNetworkCreateSerializer


class ProductCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, ActiveUsers)
    serializer_class = ProductCreateSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, ActiveUsers)
    serializer_class = ProductListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, ActiveUsers)


class FactoryListView(generics.ListAPIView):
    queryset = Factory.objects.all()
    permission_classes = (IsAuthenticated, ActiveUsers)
    serializer_class = FactoryListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title"]
    ordering = ["title"]


class FactoryCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, ActiveUsers)
    serializer_class = FactoryCreateSerializer


class FactoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = (IsAuthenticated, ActiveUsers)


class RetailNetworkListView(generics.ListAPIView):
    queryset = RetailNetwork.objects.all()
    permission_classes = (IsAuthenticated, ActiveUsers)
    serializer_class = RetailNetworkSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]


class RetailNetworkCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, ActiveUsers)
    serializer_class = RetailNetworkCreateSerializer


class RetailNetworkView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = (IsAuthenticated, ActiveUsers)


class PrivateBusinessmanListView(generics.ListAPIView):
    queryset = PrivateBusinessman.objects.all()
    permission_classes = (IsAuthenticated, ActiveUsers)
    serializer_class = PrivateBusinessmanListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]


class PrivateBusinessmanCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, ActiveUsers)
    serializer_class = PrivateBusinessmanCreateSerializer


class PrivateBusinessmanView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrivateBusinessman.objects.all()
    serializer_class = PrivateBusinessmanSerializer
    permission_classes = (IsAuthenticated, ActiveUsers)
