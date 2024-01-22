from datetime import datetime

from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest,
                         HttpResponseNotFound)
from .forms import UserForm
from .models import Company,Product
# Create your views here.


# получение данных из бд
def index(request):
    products = Product.objects.all()
    return render(request,"index.html",{"products":products})


# добавление данных из бд
def create(request):
    create_companies()  # добавляем начальные данные для компаний

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.company_id = request.POST.get("company")
        product.save()
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    companies = Company.objects.all()
    return render(request, "create.html", {"companies": companies})


# изменение данных в бд
def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get("name")
            product.price = request.POST.get("price")
            product.company_id = request.POST.get("company")
            product.save()
            return HttpResponseRedirect("/")
        else:
            companies = Company.objects.all()
            return render(request, "edit.html", {"product": product, "companies": companies})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

def create_companies():
    if Company.objects.all().count() == 0:
        Company.objects.create(name="IP PIROGOV")
        Company.objects.create(name="IP VANT")
        Company.objects.create(name="IP GADZ")