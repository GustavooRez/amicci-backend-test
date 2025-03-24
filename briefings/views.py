from rest_framework import viewsets
from .models import Category, Retailer, Vendor, Briefing
from .serializers import CategorySerializer, RetailerSerializer, VendorSerializer, BriefingSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

class BriefingViewSet(viewsets.ModelViewSet):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
