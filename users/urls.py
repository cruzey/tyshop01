from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("userModify", views.userModify_view, name="userModify"),
    path("mypage", views.mypage_view, name="mypage"),
    path("order/<int:product_pk>/", views.order_view, name="order"),
    # path("orderDetail/<int:cart_pk>/", views.orderDetail_view, name="orderDetail"),
    path("orderDel/<int:cart_pk>/", views.orderDel_view, name="orderDel"),
    path("payinfo/<int:cart_pk>/", views.payinfo_view, name="payinfo"),
    path("pay/<int:cart_pk>/", views.pay_view, name="pay"),
]