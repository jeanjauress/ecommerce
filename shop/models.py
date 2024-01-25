from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-date_added']
  def __str__(self):
    return self.name

class Product(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  price = models.FloatField()
  category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
  image = models.CharField(max_length=5000)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-date_added']
  def __str__(self):
    return self.title

class Commande(models.Model):
  items = models.CharField(max_length=300)
  nom = models.CharField(max_length=150)
  email = models.EmailField()
  address = models.CharField(max_length=200)
  ville = models.CharField(max_length=200)
  pays = models.CharField(max_length=200)
  zipcode = models.CharField(max_length=200)
  date_commande = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-date_commande']
    
  def __str__(self):
    return self.nom
  