from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from tyadmins.models import Product
from .models import Cart
from iamport import Iamport
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

User = get_user_model()

def login_view(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    elif request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('tyhome:index')
        else:
            return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')

def signup_view(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phonenum = request.POST.get('phone_number')
        
        user = User.objects.create_user(username, email, password)
        print(user)
        user.first_name = first_name
        user.last_name = last_name
        user.address = address
        user.phonenum = phonenum
        user.save()

        return redirect('users:login')

    return render(request, 'users/signup.html')

def userModify_view(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.pk)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.address = request.POST.get('address')
        user.email = request.POST.get('email')
        user.phonenum = request.POST.get('phone_number')
        user.save()

        return redirect('users:mypage')
    return render(request, 'users/modify.html')

def mypage_view(request):
    if request.method == 'GET':
        user = User.objects.get(pk=request.user.pk)
        orders = Cart.objects.filter(user_id=request.user.pk).exclude(order_id=None)
        context = {
            'user': user,
            'orders': orders
        }
        return render(request, 'users/mypage.html', context)

def order_view(request, product_pk):
    customer = User.objects.get(pk=request.user.pk)
    prod = Product.objects.get(pk=product_pk)
    order = Cart(
        number = request.POST.get('number'),
        product = prod,
        user = customer
    )
    order.save()
    context = {
        'order': order,
    }
    return render(request, 'users/orderinfo.html', context)

def orderDel_view(request, cart_pk):
    order = Cart.objects.get(pk=cart_pk)
    order.delete()

    return redirect('users:mypage')

# def orderDetail_view(request, cart_pk):
#     order = Cart.objects.get(pk=cart_pk)
#     context = {
#         'order': order,
#     }
#     return render(request, 'users/orderinfo.html', context)

def payinfo_view(request, cart_pk):
    order = Cart.objects.get(pk=cart_pk)
    iamport = Iamport(imp_key=settings.IAMPORT_KEY, imp_secret=settings.IAMPORT_SECRET)
    response = iamport.find(imp_uid=order.order_id)
    context = {
        'order': order,
        'rsp': response,
    }
    return render(request, 'users/payinfo.html', context)

@csrf_exempt
def pay_view(request, cart_pk):
    iamport = Iamport(imp_key=settings.IAMPORT_KEY, imp_secret=settings.IAMPORT_SECRET)
    order = Cart.objects.get(pk=cart_pk)
    context = {
        'order': order,
    }
    if request.method == 'POST' and request.is_ajax():
        imp_uid = request.POST.get('imp_uid')
        print(imp_uid)
        product_price = order.number * order.product.price
        if iamport.is_paid(product_price, imp_uid=imp_uid):
            # return JsonResponse({'message': "일반 결제 성공"},json_dumps_params = {'status': "success"})
            order.order_id = imp_uid
            order.save()
            return JsonResponse({'status': "success", 'message': "일반 결제 성공"})
        else:
            # return JsonResponse({'message': "위조된 결제시도"},json_dumps_params = {'status': "forgery"})
            order.delete()
            return JsonResponse({'status': "forgery", 'message': "위조된 결제시도"})
   
    return render(request, 'users/pay.html', context)