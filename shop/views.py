from django.shortcuts import render
from .models import Product, Commande
from django.core.paginator import Paginator

# Create your views here.
def index(request):
  product_object = Product.objects.all()
  item_name = request.GET.get('item-name')
  if item_name != '' and item_name is not None:
    product_object = Product.objects.filter(title__icontains=item_name)
  paginator = Paginator(product_object, 4)
  page = request.GET.get('page')
  product_object = paginator.get_page(page)
  return render(request, 'shop/index.html', {'product_object':product_object})

def detail(request, myid):
  product = Product.objects.get(id=myid)
  return render(request, 'shop/detail.html', {'product':product})

def checkout(request):
  if request.method == 'POST':
    items = request.POST.get('items')
    nom = request.POST.get('nom')
    email = request.POST.get('email')
    address = request.POST.get('address')
    ville = request.POST.get('ville')
    pays = request.POST.get('pays')
    zipcode = request.POST.get('zipcode')
    com = Commande(items=items, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode)
    com.save()
  return render(request, 'shop/checkout.html')
