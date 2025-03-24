from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, RetailerViewSet, VendorViewSet, BriefingViewSet

# Criando um router para gerar as rotas automaticamente
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'retailers', RetailerViewSet)
router.register(r'briefings', BriefingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Inclui todas as rotas do router
]
