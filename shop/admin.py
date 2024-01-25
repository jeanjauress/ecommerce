from django.contrib import admin
from .models import Category, Product, Commande

# Register your models here.
class AdminCategory(admin.ModelAdmin):
  list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
  list_display = ('title', 'price', 'date_added')

class AdminCommande(admin.ModelAdmin):
  list_display = ('nom', 'email','address', 'ville', 'date_commande')
  
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Commande, AdminCommande)
