from django.contrib import admin
from .models import Product_num,inv_Post

class Product_num_Admin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

class inv_Post_Admin(admin.ModelAdmin):
    list_display = ('id','product_num','quantity')
    list_display_links = ('id','product_num','quantity')

admin.site.register(Product_num,Product_num_Admin)
admin.site.register(inv_Post,inv_Post_Admin)