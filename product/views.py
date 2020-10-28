from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, FormView, UpdateView
from .forms import ProductForm, ProductFilterForm, ImportCategoriesForm
from .models import Product, Category

from django.contrib import messages

class InitialView(ListView):
    """
    Initial screen. Shows a screen with a list of products, a left side menu, 
    and filters to search for products
    """
    template_name = 'product/main.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_filter'] = ProductFilterForm()
        return context

    def get_queryset(self):
        queryset = Product.objects.all()
        if 'name' in self.request.GET:
            queryset = queryset.filter(name__icontains=self.request.GET.get('name'))
        if 'description' in self.request.GET:
            queryset = queryset.filter(description__icontains=self.request.GET.get('description'))
        if 'category' in self.request.GET:
            if self.request.GET.get('category'):
                queryset = queryset.filter(
                    category=Category.objects.get(id=self.request.GET.get('category'))
                )
        if 'price_min' and 'price_max' in self.request.GET:
            if self.request.GET.get('price_min') and self.request.GET.get('price_max'):
                if float(self.request.GET.get('price_min')) > float(self.request.GET.get('price_max')):
                    messages.error(self.request, 'Invalid prices')
                else:
                    queryset = queryset.filter(
                        price__gte=self.request.GET.get('price_min'),
                        price__lte=self.request.GET.get('price_max')
                    )
            elif self.request.GET.get('price_min'):
                queryset = queryset.filter(
                    price__gte=self.request.GET.get('price_min')
                )
            elif self.request.GET.get('price_max'):
                queryset = queryset.filter(
                    price__lte=self.request.GET.get('price_max')
                )
        return queryset

class CreateView(FormView):
    """
    CreateView. Shows a screen with the form to create a new product
    """
    template_name = 'product/create.html'
    form_class = ProductForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Product added!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid data.')
        return super().form_invalid(form)

class EditView(UpdateView):
    """
    EditView Shows a screen with the form to update an existing product
    """
    model = Product
    fields = ['category', 'name', 'description', 'price']
    template_name = 'product/update.html'
    success_url = '/'

    def form_valid(self, form):
        self.object.save()
        return super().form_valid(form)

class DeleteView(View):
    """
    DeleteView. Displays a message on success
    """
    def get(self, request, **kwargs):
        product = Product.objects.get(id=kwargs['product_id'])
        product.delete()
        messages.success(request, 'Product deleted.')
        return redirect('product:initial')

class ImportCategoriesView(FormView):
    """
    ImportCategoriesView. Displays a button to search for the file and another to send.
    """
    template_name = 'product/import_categories.html'
    form_class = ImportCategoriesForm
    success_url = '/'

    def form_valid(self, form):
        if form.checking_extension(form.cleaned_data['file']).lower() == 'csv':
            ok = form.import_csv(self.request.FILES['file'])
            if ok:
                messages.success(self.request, 'Categories added.')
            else:
                messages.error(self.request, 'Error reading file.')
        else:
            messages.error(self.request, 'Error reading file.')
        return super().form_valid(form)
