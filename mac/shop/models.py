from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50,default="")
    product_sub_category = models.CharField(max_length=50,default="")
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300,null=True)
    product_pub_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    product_images = models.ImageField(upload_to="shop/pro_images",default="")

    def __str__(self) :
        return self.product_name 
