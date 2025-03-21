from django.contrib import admin

from fifthapp.models import ArticlesModel, OffersModel, CategoryModel, BooksModel, CartModel, WishlistModel, OrderModel, \
    OrderItemModel

# Register your models here.
admin.site.register(ArticlesModel)
admin.site.register(OffersModel)
admin.site.register(CategoryModel)
admin.site.register(BooksModel)
admin.site.register(CartModel)
admin.site.register(WishlistModel)



class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    extra = 0  # Do not add extra empty forms

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "status", "total_price")
    list_filter = ("status", "created_at")
    search_fields = ("user__username","created_at", "id")
    inlines = [OrderItemInline]  # Show order items inside order admin page

admin.site.register(OrderModel, OrderAdmin)
admin.site.register(OrderItemModel)