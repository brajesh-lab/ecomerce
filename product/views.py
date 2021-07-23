from django.shortcuts import render
from .models import Product
# Create your views here.
def product(request):
    if request.method == "POST":
        photo = request.POST.get('files')
        name = request.POST.get("name")
        weight = request.POST.get("weight")
        price = request.POST.get("price")
        product1 = Product(photo=photo,name=name,weight=weight,price=price)
        product1.save()
    return render(request,'product.html')
def detail(request):
    item =Product.objects.all()
    context = {'item':item}
    return render(request,'detail.html', context)