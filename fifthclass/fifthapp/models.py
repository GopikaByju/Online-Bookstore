from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ArticlesModel(models.Model):
    article_title=models.CharField(max_length=100,null=True,blank=True)
    article_date=models.DateField(null=True,blank=True)
    article_desc=models.TextField(null=True,blank=True)
    article_image=models.ImageField(null=True, blank=True, upload_to='articles')

    def __str__(self):
        return self.article_title

class OffersModel(models.Model):
    offer_name = models.CharField(max_length=100, null=True, blank=True)
    offer_author = models.CharField(max_length=100, null=True, blank=True)
    prev_price = models.DecimalField(max_digits=300,decimal_places=2,null=True,blank=True)
    offer_price = models.DecimalField(max_digits=300,decimal_places=2,null=True,blank=True)
    offer_details=models.TextField(null=True,blank=True)
    offer_image = models.ImageField(null=True, blank=True, upload_to='offers')

    def __str__(self):
        return self.offer_name


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class BooksModel(models.Model):
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True,blank=True,related_name='books')
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    publication_date = models.DateField( null=True, blank=True)
    isbn = models.CharField(max_length=50, null=True, blank=True)
    edition = models.CharField(max_length=100, blank=True, null=True)
    pages = models.IntegerField( null=True, blank=True)
    language = models.CharField(max_length=100, default="English", null=True, blank=True)
    cover_type = models.CharField(max_length=50, choices=[('Hardcover', 'Hardcover'), ('Paperback', 'Paperback'), ('eBook', 'eBook')])
    rating = models.FloatField(default=0.0, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField( null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    book_image = models.ImageField(upload_to='books', blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    paper_quality = models.CharField(max_length=100, blank=True, null=True)
    print_type = models.CharField(max_length=100, choices=[('Black & White', 'Black & White'), ('Color', 'Color')], default='Black & White')
    binding = models.CharField(max_length=100, choices=[('Perfect Bound', 'Perfect Bound'), ('Spiral Bound', 'Spiral Bound')], default='Perfect Bound')


    best_seller = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1,null=True,blank=True)

    def __str__(self):
        return f"{self.book}"

    def total_price(self):
        return self.quantity * self.book.price

class WishlistModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.book}"

    class Meta:
        unique_together = ('user', 'book')  # Prevent duplicate wishlisted items

class OrderModel(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)  # Order belongs to a user
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    status = models.CharField(max_length=20, choices=[('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')],null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items",null=True,blank=True)
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)  # Price at purchase time

    def __str__(self):
        return f"{self.quantity} x {self.book.title} in Order {self.order.id}"



