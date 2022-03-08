from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='shopapp'

urlpatterns =[

    path('' , views.product_list, name='product_list'),
    path('<slug:category_slug>/' , views.product_list , name='product_list_by_category'),
    path( '' , views.product_detail, name='product_detail'),
    path('<int:id>/<slug:slug>/' , views.product_detail , name='product_detail')
    
]









