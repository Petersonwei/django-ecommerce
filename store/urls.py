from django.urls import path

from . import views

urlpatterns = [
    
    #Home page
    path('', views.store, name='store'),

    #Product info
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),

    #Category list
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
]


