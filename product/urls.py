from django.urls import path
from .views import InitialView, CreateView, EditView, DeleteView, ImportCategoriesView

urlpatterns = [
    path('', InitialView.as_view(), name='initial'),
    path('create/', CreateView.as_view(), name='create'),
    path('edit/<int:pk>/', EditView.as_view(), name='edit'),
    path('delete/<int:product_id>/', DeleteView.as_view(), name='delete'),
    path('import-categories/', ImportCategoriesView.as_view(), name='import-categories'),
]
