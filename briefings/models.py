from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Retailer(models.Model):
    name = models.CharField(max_length=255)
    vendors = models.ManyToManyField(Vendor)
    
    def __str__(self):
        return self.name

class Briefing(models.Model):
    name = models.CharField(max_length=255)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    responsible = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    release_date = models.DateField()
    availabe = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
