from django.db import models
from django.contrib.auth.models import AbstractUser

# Property model
class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Custom User model
class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics/')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Thêm related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Thêm related_name
        blank=True,
    )

# Review model
class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews_seller')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews_user')
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.property.name if self.property else 'Seller'}"

# PropertyImage model
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    caption = models.TextField(blank=True)

    def __str__(self):
        return f"Image for {self.property.name}"

# Favorite model
class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} favorite {self.property.name}"
