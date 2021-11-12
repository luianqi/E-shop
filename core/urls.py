"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from users.views import *
from products.views import *
from cart.views import *
from orders.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view()),
    path("product-list/", ProductList.as_view(), name="product-list"),
    path("product-detail/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
    path("comment-list/", CommentList.as_view(), name="comment-list"),
    path("comment-detail/<int:pk>/", CommentDetail.as_view(), name="comment-detail"),
    path("reply-list/", ReplyList.as_view(), name="reply-list"),
    path("reply-detail/<int:pk>/", ReplyDetail.as_view(), name="reply-detail"),
    path("category/", CategoryList.as_view(), name="category"),
    path("cart/", CartAdd.as_view(), name="add"),
    # path('cart-detail/<int:pk>', CartDetail.as_view()),
    path("order/", OrderView.as_view())
    # path('getorder/', OrderListView.as_view()),
]
