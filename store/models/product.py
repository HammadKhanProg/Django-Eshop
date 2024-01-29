from django.db import models
from .category import Category

class Product (models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to="uploads/products")
    
    @staticmethod
    def products_id (ids):
        return Product.objects.filter(id__in=ids)
    
    def get_all_products ():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_id (category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
