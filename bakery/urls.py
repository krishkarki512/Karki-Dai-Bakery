from django.urls import path
from .views import (
    home,
    cake_detail,
    search_cakes,
    signup_view,
    login_view,
    logout_view,
    cart_view,
    add_to_cart,
    remove_from_cart,
    checkout,
    order_success,
    order_history,
)

urlpatterns = [
    path('', home, name='home'),
    path('cake/<int:cake_id>/', cake_detail, name='cake_detail'),
    path('search/', search_cakes, name='search'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Cart URLs
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:cake_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:cake_id>/', remove_from_cart, name='remove_cart'),
    path("cart/", cart_view, name="cart"),
    path("update-cart/<int:cake_id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:cake_id>/", remove_from_cart, name="remove_from_cart"),
    path("checkout/", checkout, name="checkout"),
    path("order-success/<int:order_id>/", order_success, name="order_success"),
    path("orders/", order_history, name="order_history"),
]
