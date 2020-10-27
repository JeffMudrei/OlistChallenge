from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, FormView, UpdateView
from .forms import ProductForm, ProductFilterForm, ImportCategoriesForm
from .models import Product, Category

from django.contrib import messages

class InitialView(ListView):
    '''
    Initial screen. Shows a screen with ...
    '''
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
    model = Product
    fields = ['category', 'name', 'description', 'price']
    template_name = 'product/update.html'
    success_url = '/'

    def form_valid(self, form):
        self.object.save()
        return super().form_valid(form)

class DeleteView(View):
    def get(self, request, **kwargs):
        product = Product.objects.get(id=kwargs['product_id'])
        product.delete()
        messages.success(request, 'Product deleted.')
        return redirect('product:initial')

class ImportCategoriesView(FormView):
    template_name = 'product/import_categories.html'
    form_class = ImportCategoriesForm
    success_url = '/'

    def form_valid(self, form):
        ok = form.import_csv(self.request.FILES['file'])
        if ok:
            messages.success(self.request, 'Categories added.')
        else:
            messages.error(self.request, 'Error reading file.')
        return super().form_valid(form)

#################################################################

# rm db.sqlite3; rm */migrations/00*; python manage.py makemigrations; python manage.py migrate; python manage.py createsuperuser; python manage.py runserver


# from django.views import View
#
# class InitialView(View):
#     def get(self, request, **kwargs):
#         context = {}
#         context['object_list'] = Product.objects.all()
#         return render(request, 'product/main.html', context)
