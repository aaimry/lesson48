from django.urls import path

from store.views import product_view, product_add_view, product_check_view, update_product_view, product_delete_view, \
    product_category_view

urlpatterns = [
    path('', product_view, name='index'),
    path('add/', product_add_view, name='product_add'),
    path('check/<int:pk>', product_check_view, name='product_check'),
    path('check/<int:pk>/update', update_product_view, name='product_update'),
    path('check/<int:pk>/delete', product_delete_view, name='product_delete'),
    path('check/<str:category>', product_category_view, name='product_category')
]
