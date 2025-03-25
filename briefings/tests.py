from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Vendor, Retailer, Briefing

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Categoria", description="Descrição da categoria")

        self.vendor = Vendor.objects.create(name="Vendor")
        
        self.retailer = Retailer.objects.create(name="Retailer")
        self.retailer.vendors.set([self.vendor])

        self.briefing = Briefing.objects.create(
            name="Briefing",
            retailer=self.retailer,
            responsible="Equipe",
            category=self.category,
            release_date="2025-04-01",
            availabe="Disponível"
        )
        
    # Category POST, GET, UPDATE
    def test_create_category(self):
        """Create a new category"""
        data = {"name": "Categoria", "description": "Descrição da categoria"}
        response = self.client.post("/api/categories/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_categories(self):
        """Get Categories"""
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_category(self):
        """Update Category"""
        data = {"name": "Categoria atualizada", "description": "Descrição atualizada"}
        response = self.client.put(f"/api/categories/{self.category.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "Categoria atualizada")
        self.assertEqual(self.category.description, "Descrição atualizada")
        
    # Vendor POST, GET, UPDATE
    def test_create_vendor(self):
        """Create a new vendor"""
        data = {"name": "Vendor"}
        response = self.client.post("/api/vendors/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_vendors(self):
        """Get Vendors"""
        response = self.client.get("/api/vendors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_vendor(self):
        """Update Vendor"""
        data = {"name": "Vendor atualizado"}
        response = self.client.put(f"/api/vendors/{self.vendor.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.name, "Vendor atualizado")

    # Retailer POST, GET, UPDATE
    def test_create_retailer(self):
        """Create Retailer"""
        data = {"name": "Retailer", "vendors": [self.vendor.id]}
        response = self.client.post("/api/retailers/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_retailers(self):
        """Get Retailers"""
        response = self.client.get("/api/retailers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_update_retailer(self):
        """Update Retailer"""
        data = {"name": "Retailer atualizado", "vendors": [self.vendor.id]}
        response = self.client.put(f"/api/retailers/{self.retailer.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.retailer.refresh_from_db()
        self.assertEqual(self.retailer.name, "Retailer atualizado")

    # Briefing POST, GET, UPDATE
    def test_create_briefing(self):
        """Create Briefing"""
        data = {
            "name": "Briefing",
            "retailer": self.retailer.id,
            "responsible": "Equipe",
            "category": self.category.id,
            "release_date": "2025-04-25",
            "availabe": "Disponível"
        }
        response = self.client.post("/api/briefings/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_briefings(self):
        """Get all Briefing"""
        response = self.client.get("/api/briefings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_update_briefing(self):
        """Update Briefing"""
        data = {
            "name": "Briefing Atualizado",
            "retailer": self.retailer.id,
            "responsible": "Equipe Atualizada",
            "category": self.category.id,
            "release_date": "2025-04-25",
            "availabe": "Indisponível"
        }
        response = self.client.put(f"/api/briefings/{self.briefing.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.briefing.refresh_from_db()
        self.assertEqual(self.briefing.name, "Briefing Atualizado")
        self.assertEqual(self.briefing.responsible, "Equipe Atualizada")
        self.assertEqual(self.briefing.availabe, "Indisponível")

    # All Deletes
    def test_delete_category(self):
        """Delete Category"""
        response = self.client.delete(f"/api/categories/{self.category.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_delete_vendor(self):
        """Delete Vendor"""
        response = self.client.delete(f"/api/vendors/{self.vendor.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vendor.objects.count(), 0)
        
    def test_delete_retailer(self):
        """Delete Retailer"""
        response = self.client.delete(f"/api/retailers/{self.retailer.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Retailer.objects.count(), 0)
        
    def test_delete_briefing(self):
        """Delete Briefing"""
        response = self.client.delete(f"/api/briefings/{self.briefing.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Briefing.objects.count(), 0)