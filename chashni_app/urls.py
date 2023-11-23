from django.urls import path
from . import views

urlpatterns = [
   path('shop/',views.shop,name='shop'),
   path('product_detail/<int:id>',views.product_detail,name='product_detail'),
   path('category-products/<int:id>',views.category_products, name='category_products'),
   path('cart/',views.cart,name='cart'),
   path('show_cart/',views.show_cart,name='show_cart'),
   path('delete/<int:id>',views.delete,name='delete'),
   path('packaging/',views.packaging,name='packaging'),
   path('menu/',views.menu,name='menu'),
   path('home/',views.home,name='home'),
   path('coperate/',views.coperate,name='coperate'),
   path('edit_profile/',views.edit_profile,name='edit_profile'),
   path('change_password/',views.change_password,name='change_password'),
   path('login/',views.login_user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('checkout/',views.checkout,name='checkout'),
   path('create_account/',views.create_account,name='create_account'),
   path('category/<int:id>',views.category_item,name='category')
]