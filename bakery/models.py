from django.db import models
from django.contrib.auth.models import User


# ================= CAKE MODEL =================
class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='cakes/')
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)   # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ================= NEWSLETTER MODEL =================
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# ================= ORDER MODEL =================
class Order(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


# ================= ORDER ITEM MODEL =================
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cake.name} x {self.quantity}"