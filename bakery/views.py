from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Cake, Newsletter, Order, OrderItem
from .forms import SignupForm


# ================= HOME =================
def home(request):
    cakes = Cake.objects.filter(available=True)
    return render(request, "home.html", {"cakes": cakes})


# ================= SIGNUP =================
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


# ================= LOGIN =================
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect("home")


# ================= SEARCH =================
def search_cakes(request):
    query = request.GET.get("q", "")
    cakes = Cake.objects.filter(name__icontains=query, available=True)

    return render(request, "search.html", {
        "cakes": cakes,
        "query": query
    })


# ================= CAKE DETAIL =================
def cake_detail(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    cart = request.session.get("cart", {})
    in_cart = str(cake_id) in cart

    return render(request, "cake_detail.html", {
        "cake": cake,
        "in_cart": in_cart
    })


# ================= ADD TO CART =================
def add_to_cart(request, cake_id):
    cart = request.session.get("cart", {})

    cake = get_object_or_404(Cake, id=cake_id)
    cake_id = str(cake_id)

    if cake_id in cart:
        cart[cake_id]["quantity"] += 1
    else:
        cart[cake_id] = {
            "name": cake.name,
            "price": float(cake.price),
            "image": cake.image.url,
            "quantity": 1
        }

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# ================= UPDATE QUANTITY =================
def update_cart(request, cake_id):
    cart = request.session.get("cart", {})
    cake_id = str(cake_id)

    if cake_id in cart:
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart[cake_id]["quantity"] = quantity
        else:
            del cart[cake_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# ================= REMOVE ITEM =================
def remove_from_cart(request, cake_id):
    cart = request.session.get("cart", {})
    cake_id = str(cake_id)

    if cake_id in cart:
        del cart[cake_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# ================= CART PAGE =================
def cart_view(request):
    cart = request.session.get("cart", {})
    total = sum(item["price"] * item["quantity"] for item in cart.values())

    return render(request, "cart.html", {
        "cart": cart,
        "total": total
    })


# ================= CHECKOUT =================
@login_required
def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        return redirect("home")

    total = sum(item["price"] * item["quantity"] for item in cart.values())

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            address=address,
            phone=phone,
            total_amount=total
        )

        for cake_id, item in cart.items():
            cake = Cake.objects.get(id=cake_id)

            OrderItem.objects.create(
                order=order,
                cake=cake,
                quantity=item["quantity"],
                price=item["price"]
            )

        # Clear cart after order
        request.session["cart"] = {}
        request.session.modified = True

        return redirect("order_success", order_id=order.id)

    return render(request, "checkout.html", {"total": total})


# ================= ORDER SUCCESS =================
@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "order_success.html", {"order": order})


# ================= ORDER HISTORY =================
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "order_history.html", {"orders": orders})