from django.shortcuts import render,redirect
from .models import Product,Category,Cart
from django.contrib import messages
from django.http import HttpResponse
from .forms.orderform import OrderForm
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from .forms.usercreationform import SignupForm
from .forms.userupdateform import UserUpdateForm
from .forms.changepassword import PasswordUpdateForm

# Create your views here.
def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid:
            form.save()
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, 'Error generated')
        return redirect('edit_profile')
    else:
        form = UserUpdateForm(instance=request.user)

    # return HttpResponse(form)
    return render(request, 'edit_profile.html', {'form': form})


    # return render(request,'edit_profile.html')
def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=='POST':
        form=PasswordUpdateForm(request.user,request.POST)
        if form.is_valid():
           user= form.save()
           update_session_auth_hash(request,user)
           messages.success(request,'password changed.')
           return redirect('edit_profile')
        else:
           messages.error(request,'password changed.')
           return redirect('change_password')
    else:
        form=PasswordUpdateForm(request.user)

    return render(request,'change_password.html',{'form':form})

def shop(request):
    # products=Product.objects.all()
    # category_object = Category.objects.get(pk=id)
    # return HttpResponse(category_object)
    # category_name = category_object.name
    # products = Product.objects.filter(category)

    categories = Category.objects.all()
    # return render(request,'shop.html' ,{'products':products,'categories':categories})
    return render(request,'shop.html' ,{'categories':categories})

def product_detail(request,id):
    product=Product.objects.get(pk=id)

    return render(request, 'product-detail.html',{'product':product})


def category_products(request,id):
    category_object = Category.objects.get(pk=id)
    # return HttpResponse(category_object)
    category_name = category_object.name
    products = Product.objects.filter(category = category_object )

    categories = Category.objects.all()
    # return HttpResponse(categories)
    return render(request,'shop.html',{'products':products ,'categories': categories,'category_name':category_name})


def cart(request):
    if request.method=='POST':
        product_id=request.POST['product_id']
        qty=int(request.POST['qty'])
        user=request.user
        product=Product.objects.get(pk=product_id)
        try:
            cart_item=Cart.objects.get(product=product,order_id=0)
        except:
            cart_item=False
        
        if cart_item is False:
            sub_total=qty*product.price
            cart=Cart(product=product,sub_total=sub_total,qty=qty,user=user)
            cart.save()
            # messages.success(request,'item added to cart')
            # return redirect('shop')
        else:
            cart_item.qty=cart_item.qty+qty
            cart_item.sub_total=qty*product.price
            cart_item.save()
    
        messages.success(request,'Product added to Cart successfully!!')
        return redirect('show_cart')

def show_cart(request):
    
    cart_items=Cart.objects.filter(user=request.user,order_id=0)
    grand_total=0
    for item in cart_items:
        grand_total += item.sub_total
    return render(request,'cart.html',{'cart_items':cart_items,'grand_total':grand_total})    


def delete(request,id):
    cart_item=Cart.objects.get(pk=id)
    # # cart_item=instance = get_object_or_404(Cart, id=id)
    if cart_item:
        cart_item.delete()
        # return HttpResponse('deleted')
        messages.success(request,'cart item deleted successfully')
        return redirect('show_cart')
    else:
        messages.error(request,'cart item does not exist')
        return redirect('show_cart')
    
def checkout(request):
    cart_items=Cart.objects.filter(user=request.user,order_id=0)
    grand_total=0
    for item in cart_items:
        grand_total += item.sub_total
    if cart_items:
        if request.method=='POST':
            form=OrderForm(request.POST)
            if form.is_valid:
                form_order=form.save(commit=False)
                if request.user is not None:
                    form_order.user=request.user
                if request.POST.get('order_amount'):
                    form_order.order_amount=request.POST.get('order_amount')
                if request.POST.get('payment_mod'):
                    form_order.payment_mod=request.POST.get('payment_mod')
                if request.POST.get('delivery_method'):
                    form_order.delivery_method=request.POST.get('delivery_method')
                form_order.save()
                #   cart_items = Cart.objects.filter(user=request.user,order_id=0)
                for cart_item in cart_items:
                    cart_item.order_id = form_order.id
                    cart_item.save()
                
                messages.success(request,'Order is placed ')
                return redirect('shop')
            else:   
                messages.error(request,'Something went wrong!')
                return redirect('cart')
        else:
            form=OrderForm()
        return render(request,'checkout.html',{'grand_total':grand_total,'form':form,'cart_items':cart_items})
    else:
        messages.error(request,'cart is empty!')
        return redirect('show_cart')
    # return render(request,'checkout.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=email , password =password )
        if user is not None:
            login(request, user)
            messages.success(request,'Logged in successfull.')
            return redirect('shop')
        else:
            messages.error(request,'Invalid credentials!!!')
            return redirect('login')    
    else:
        return render(request,'login.html')
def logout_user(request):
    logout(request)
    messages.success(request, 'logged out successfull.')
    return redirect('login')

def create_account(request):
    if request.method=='POST':

        form =SignupForm(request.POST )
        if form.is_valid():
            form.save()
            messages.success(request,'Registered Successfully!!! kindly login')
            return redirect('login')
    # return HttpResponse(form)
        else:
            messages.error(request,'Invalid credentials')
            return HttpResponse(form.errors)

            # return redirect('create_account')
        
    else:
        form=SignupForm()
        return render(request,'create_account.html',{'form':form})
    
    # return render(request,'create_account.html')

def home(request):
    # product = Product.objects.all()
    return render(request,'home.html')

def category_item(request,id):
    category=Category.objects.get(pk=id)
    products=Product.objects.filter(category=category)
    # return HttpResponse(products)
    return render(request,'mithai.html',{"products":products,"category":category})
def packaging(request):
    return render(request,'packaging.html')

def menu(request):
    return render(request,'menu.html')


def coperate(request):
    return render(request,'coperate.html')