from store.models import Product,Category
from django.db.models import Count
from django.urls import reverse_lazy
from store.forms import ProductForm
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    

class ProductOwnerMixin(UserPassesTestMixin):
    
    def test_func(self):
        return  self.get_object().user == self.request.user  
     
class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('store:index')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProductDeleteView(LoginRequiredMixin,ProductOwnerMixin,DeleteView):
    model = Product
    template_name = 'delete_product.html'
    pk_url_kwarg = 'product_id'
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
 
