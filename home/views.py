from django.shortcuts import render

# Create your views here.
from django.views import View
from home.models import *


class BaseView(View):
    views = ()

class HomeView(BaseView):
    def get(self, request):
        self.views['catagories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['ads1'] = Ad.objects.filter(rank=1)
        self.views['ads2'] = Ad.objects.filter(rank=2)
        self.views['ads3'] = Ad.objects.filter(rank=3)
        self.views['ads4'] = Ad.objects.filter(rank=4)
        self.views['ads5'] = Ad.objects.filter(rank=5)
        self.views['ads6'] = Ad.objects.filter(rank=6)
        self.views['ads7'] = Ad.objects.filter(rank=7)
        self.views['ads8'] = Ad.objects.filter(rank=8)
        self.views['items'] = Items.objects.all()
        self.views['new_items'] = Items.objects.filter(label='new')
        self.views['hot_items'] = Items.objects.filter(label='hot')
        self.views['sale_items'] = Items.objects.filter(label='sale')

        return render(request, 'index.html', self.views)


class ProductDetailView(BaseView):
    def get(self, request, slug):
        category = Items.objects.get(slug=slug).categogy
        self.views['detail_item'] = Items.objects.filter(slug=slug)
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['related_item'] = Items.objects.filter(category=category)

        return render(request, 'product-detail.html', self.views)
