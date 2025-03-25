from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, RetailerViewSet, VendorViewSet, BriefingViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'retailers', RetailerViewSet)
router.register(r'briefings', BriefingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
