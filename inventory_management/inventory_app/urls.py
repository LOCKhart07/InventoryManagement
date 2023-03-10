from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("", views.products, name="home"),
    path("signup", views.signup, name="signup"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("products/<cat>", views.products, name="products"),
    path("products/", views.products, name="products"),
    path("categories/", views.categories, name="categories"),
    # path("email/", views.email, name="email"),
    # path("sendmail/", views.send_email, name="sendmail"),
    path("products/update_item/", views.updateItem, name="update_item"),
    path("cart/", views.cart, name="cart"),
    path("cart/update_item/", views.updateItem, name="update_item"),
    path("update_item/", views.updateItem, name="update_item"),
    path("profile", views.profile, name="profile"),
    # path("checkout/", views.checkout, name="checkout"),
]

urlpatterns += [
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("images/favicon.ico")),
    )
]
