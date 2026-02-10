from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Cake, Newsletter
from .forms import SignupForm


# ================= HOME =================
def home(request):
    cakes = Cake.objects.all()
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

    if query:
        cakes = Cake.objects.filter(name__icontains=query)
    else:
        cakes = Cake.objects.all()

    return render(request, "search.html", {
        "cakes": cakes,
        "query": query
    })


# ================= ADD TO CART =================
def add_to_cart(request, cake_id):
    cart = request.session.get('cart', {})

    cake = get_object_or_404(Cake, id=cake_id)
    cake_id = str(cake_id)

    if cake_id in cart:
        cart[cake_id]['quantity'] += 1
    else:
        cart[cake_id] = {
            'name': cake.name,
            'price': float(cake.price),
            'image': cake.image.url,
            'quantity': 1
        }

    request.session['cart'] = cart
    request.session.modified = True

    return JsonResponse({'status': 'added'})


# ================= CART PAGE =================
def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())

    return render(request, "cart.html", {
        "cart": cart,
        "total": total
    })


# ================= REMOVE ITEM =================
def remove_from_cart(request, cake_id):
    cart = request.session.get('cart', {})
    cake_id = str(cake_id)

    if cake_id in cart:
        del cart[cake_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')
