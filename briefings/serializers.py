from rest_framework import serializers
from .models import Category, Retailer, Vendor, Briefing

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class RetailerSerializer(serializers.ModelSerializer):
    vendors = serializers.PrimaryKeyRelatedField(many=True, queryset=Vendor.objects.all())

    class Meta:
        model = Retailer
        fields = '__all__'

class BriefingSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    retailer = serializers.PrimaryKeyRelatedField(queryset=Retailer.objects.all())

    class Meta:
        model = Briefing
        fields = '__all__'
