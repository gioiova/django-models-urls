from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.http import JsonResponse
from store.models import Product,Category
from django.db.models import Count
from django.urls import reverse_lazy
from store.forms import ProductForm
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView

# Create your views here.
# def index(request):
#     products = Product.objects.order_by('price').prefetch_related('category')
#     categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
#     return render(request, 'index.html', {'products': products, 'categories': categories})

# def category_view(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     products = Product.objects.filter(category=category).order_by('price')
#     return render(request, 'category.html', {'category': category, 'products': products})

# def sale_products(request):
#     sale_products = Product.objects.filter(is_sale=True)
#     return render(request, 'sale_products.html', {'sale_products': sale_products})

# def product_detail(request,product_id):
#     product = get_object_or_404(Product,id = product_id)
#     return render(request,'product_detail.html',{'product':product})

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
        
#         return redirect('store:index')
#     else:
#         form = ProductForm()
    
#     return render(request,'add_product.html',{'form':form})



# def delete_product(request,product_id):
#     product = get_object_or_404(Product,id = product_id)
    
#     if request.method =='POST':
#         product.delete()
#         return redirect('store:index')
    
#     return render(
#         request,
#         'delete_product.html',
#         {'product':product}
#     )
    
class IndexView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products' 
    
    def get_queryset(self):
        return Product.objects.order_by('price').prefetch_related('category')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(
            product_count=Count('products')
        ).filter(product_count__gt=0)
        return context

class SaleProductListView(ListView):
    model = Product
    template_name = 'sale_products.html'
    context_object_name = 'sale_products'

    def get_queryset(self):
        return Product.objects.filter(is_sale=True)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()

        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'
    


class ProductCreateView(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('store:index')
    

class CategoryView(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'
    pk_url_kwarg = 'category_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            category=self.object
        ).order_by('price')
        return context
 
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('store:index')

