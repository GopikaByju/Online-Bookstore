from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models.fields import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from fifthapp.forms import ArticlesForm, OffersForm, CategoryForm, BooksForm
from fifthapp.models import ArticlesModel, OffersModel, BooksModel, CategoryModel, CartModel, WishlistModel, OrderModel, \
    OrderItemModel


# Create your views here.
def indexview(request):
    return render(request,'index.html')

def HomeView(request):
    return render(request,'home.html')

def AboutView(request):
    return render(request,'about.html')

def CategoryView(request):
    cat = CategoryModel.objects.all()
    return render(request,'category.html',{'cat':cat})

# def BooksView(request):
#     boo = BooksModel.objects.all()
#     return render(request,'category.html',{'boo':boo})

def BooksAdd(request):
    if request.method=='POST':
        form=BooksForm(request.POST)
        if form.is_valid():
            form.save()
    form=BooksForm()
    return render(request,'booksadd.html',{'form':form})

def BooksDisplay(request):
    boo=BooksModel.objects.all()
    return render(request,'booksdisplay.html',{'boo':boo})

def BooksEdit(request,id):
    book=get_object_or_404(BooksModel,id=id)
    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('booksdisplay')
    form = BooksForm(instance=book)
    return render(request, 'booksedit.html', {'form': form})

def BooksDelete(request,id):
    boo = get_object_or_404(BooksModel, id=id)
    boo.delete()
    return redirect('booksdisplay')

def CategoryAdd(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    form=CategoryForm()
    return render(request,'categoryadd.html',{'form':form})

def CategoryDisplay(request):
    cat=CategoryModel.objects.all()
    return render(request,'categorydisplay.html',{'cat':cat})

def CategoryEdit(request,id):
    category=get_object_or_404(CategoryModel,id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categorydisplay')
    form = CategoryForm(instance=category)
    return render(request, 'categoryedit.html', {'form': form})

def CategoryDelete(request,id):
    cat = get_object_or_404(CategoryModel, id=id)
    cat.delete()
    return redirect('categorydisplay')

def CategoryDetailsView(request,id):
    cat = get_object_or_404(CategoryModel, id=id)
    books = cat.books.all()
    return render(request, 'categorydetails.html', {'cat': cat,'books': books})

def BooksSingleDisplay(request,id):
    boo=BooksModel.objects.get(id=id)
    return render(request,'booksingle.html',{'boo':boo})

def ArticlesView(request):
    art = ArticlesModel.objects.all()
    return render(request,'articles.html',{'art':art})

def ArticlesAdd(request):
    if request.method=='POST':
        form=ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
    form=ArticlesForm()
    return render(request,'articlesadd.html',{'form':form})

def ArticlesDisplay(request):
    art=ArticlesModel.objects.all()
    return render(request,'articlesdisplay.html',{'art':art})

def ArticlesEdit(request,id):
    article=get_object_or_404(ArticlesModel,id=id)
    if request.method == 'POST':
        form = ArticlesForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articlesdisplay')
    form = ArticlesForm(instance=article)
    return render(request, 'articlesedit.html', {'form': form})

def ArticlesDelete(request,id):
    art = get_object_or_404(ArticlesModel, id=id)
    art.delete()
    return redirect('articlesdisplay')

def ArticlesSingleDisplay(request,id):
    art=ArticlesModel.objects.get(id=id)
    return render(request,'articlesingle.html',{'art':art})

def ArticleDetails(request,id):
    art=get_object_or_404(ArticlesModel,id=id)
    return render(request,'articlesdetails.html',{'art':art})

def OffersView(request):
    offer_books = BooksModel.objects.filter(discount__gt=20).order_by('-discount')
    return render(request, 'offers.html', {'offer_books': offer_books})


def BookIndividualView(request,id):
    boo = BooksModel.objects.get(id=id)
    return render(request,'bookindividual.html',{'boo':boo})

def BestSellersView(request):
    best_sellers = BooksModel.objects.filter(best_seller=True).order_by('-rating')[:6]
    return render(request, 'bestsellers.html', {'best_sellers': best_sellers})

def CareersView(request):
    return render(request,'careers.html')

def ContactUsView(request):
    return render(request,'contactus.html')

def PrivacyPolicyView(request):
    return render(request,'privacypolicy.html')

def ShippingandReturnsView(request):
    return render(request,'shipping&returns.html')

def PaymentsandRefundView(request):
    return render(request,'payments&refund.html')

def TandCView(request):
    return render(request,'t&c.html')

def ThankYouView(request):
    return render(request,'thankyou.html')

def BookListView(request):
    return render(request,'book_list.html')

@login_required
def add_to_cart(request, book_id):
    book = BooksModel.objects.get(id=book_id)
    quantity = int(request.POST.get('quantity', 1))  # Get selected quantity, default to 1

    if book.stock < quantity:
        messages.error(request, f"Not enough stock for {book.title}. Only {book.stock} left.")
        return redirect(request.META.get('HTTP_REFERER', reverse('categorydetails', args=[book.id])))  # Stay on the same page

    # Check if the item already exists in the cart
    cart_item, created = CartModel.objects.get_or_create(user=request.user, book=book)

    if created:
        cart_item.quantity = quantity  # Set quantity for new item
    else:
        cart_item.quantity += quantity  # Increase quantity if item already in cart

    cart_item.save()

    # Reduce stock immediately after adding to cart
    book.stock -= quantity
    book.save()

    messages.success(request, f"{quantity} {book.title}(s) added to your cart.")
    return redirect('cart')

@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(BooksModel, id=book_id)

    if not WishlistModel.objects.filter(user=request.user, book=book).exists():
        WishlistModel.objects.create(user=request.user, book=book)
        messages.success(request, "Book added to wishlist!")
    else:
        messages.info(request, "Book is already in your wishlist.")

    return redirect('wishlist')


def move_to_cart(request, item_id):
    # Get the wishlist item
    wishlist_item = get_object_or_404(WishlistModel, id=item_id)

    # Get the current user (assuming the user is logged in)
    user = request.user

    # Create a CartItem for the user
    cart_item = CartModel.objects.create(
        user=user,
        book=wishlist_item.book,
        quantity=1  # Set the default quantity, or get it from a form if needed
    )

    # Remove the item from the wishlist
    wishlist_item.delete()

    # Redirect to the cart page
    return redirect('cart')

@login_required
def move_to_wishlist(request, item_id):
    cart_item = get_object_or_404(CartModel, id=item_id, user=request.user)
    book = cart_item.book

    # Add book to wishlist
    WishlistModel.objects.get_or_create(user=request.user, book=book)

    # Remove item from cart
    cart_item.delete()

    messages.success(request, "Item moved to wishlist.")
    return redirect('cart')  # Redirect to the cart page


def cart_and_wishlist_count(request):
    cart_count = CartModel.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    wishlist_count = WishlistModel.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return {'cart_count': cart_count, 'wishlist_count': wishlist_count}

def cart_view(request):
    user = request.user
    cart_items = CartModel.objects.filter(user=user)

    # Debug: Print total price to console
    total_price = sum(item.book.price * item.quantity for item in cart_items)
    print("Total Price:", total_price)  # ✅ Check if this prints correctly

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def wishlist_view(request):
    wishlist_items = WishlistModel.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

def update_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartModel, id=item_id)
        book = cart_item.book  # Get the associated book

        try:
            new_quantity = int(request.POST['quantity'])
        except ValueError:
            messages.error(request, "Invalid quantity entered.")
            return redirect('cart')

        # If the new quantity is 0 or negative, remove the item from cart
        if new_quantity <= 0:
            book.stock += cart_item.quantity  # Restore stock before deleting
            book.save()
            cart_item.delete()
            messages.success(request, f"{book.title} removed from cart.")
            return redirect('cart')

        # Check stock availability (considering current cart quantity)
        available_stock = book.stock + cart_item.quantity  # Stock + what's already in cart
        if new_quantity > available_stock:
            messages.error(request, f"Not enough stock available for {book.title}. Only {available_stock} left.")
            return redirect('cart')

        # Adjust stock accordingly
        if new_quantity > cart_item.quantity:  # Increasing quantity
            book.stock -= (new_quantity - cart_item.quantity)
        else:  # Decreasing quantity
            book.stock += (cart_item.quantity - new_quantity)

        book.save()  # Save updated stock
        cart_item.quantity = new_quantity
        cart_item.save()

        messages.success(request, f"Updated {book.title} quantity to {new_quantity}.")
        return redirect('cart')  # Redirect back to the cart page

    return redirect('cart')




@login_required
def remove_from_cart(request, item_id):
    cart_item = CartModel.objects.get(id=item_id)

    book = cart_item.book
    book.stock += cart_item.quantity  # Restore the stock
    book.save()

    cart_item.delete()
    messages.success(request, "Item removed from cart and stock updated.")

    return redirect('cart')

def checkout(request):
    user = request.user
    cart_items = CartModel.objects.filter(user=user)

    if not cart_items.exists():
        return render(request, 'checkout.html', {'error': 'Your cart is empty!'})

    total_price = sum(item.book.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        order = OrderModel.objects.create(user=user, total_price=total_price)

        for item in cart_items:
            book = item.book

            if book.stock < item.quantity:
                messages.error(request, f"Not enough stock for {book.title}. Only {book.stock} left.")
                return redirect('cart')

            book.stock -= item.quantity  # Reduce stock
            book.save()

            OrderItemModel.objects.create(
                order=order,
                book=book,
                quantity=item.quantity,
                price=item.book.price * item.quantity
            )

        cart_items.delete()

        messages.success(request, "Your order has been placed successfully!")
        return redirect('order_success')

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})

def order_success(request):
    return render(request, 'order_success.html')

def CartBookIndividual(request,id):
    boo = BooksModel.objects.get(id=id)
    return render(request, 'cartbookindividual.html',{'boo':boo})

def WishlistBookIndividual(request,id):
    boo = BooksModel.objects.get(id=id)
    return render(request, 'wishlistbookindividual.html',{'boo':boo})

@login_required
def place_order(request):
    if request.method == 'POST':
        cart_items = CartModel.objects.filter(user=request.user)

        if not cart_items:
            messages.error(request, "Your cart is empty. Please add items to your cart.")
            return redirect('cart')

        total_price = sum([item.book.price * item.quantity for item in cart_items])
        order = OrderModel.objects.create(user=request.user, total_price=total_price)

        for item in cart_items:
            book = item.book

            # Ensure stock check (this should already be handled in add_to_cart)
            if book.stock < 0:  # Stock should not be negative at this point
                messages.error(request, f"Stock error for {book.title}.")
                return redirect('cart')

            OrderItemModel.objects.create(
                order=order,
                book=book,
                quantity=item.quantity,
                price=item.book.price
            )

        cart_items.delete()  # Empty the cart after checkout

        messages.success(request, "Your order has been placed successfully!")
        return redirect('order_success')

    return redirect('cart')

def register_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful.You can now log in")
            return redirect('login')
        else:
            messages.error(request,"Registration failed.Please correct the errors below")
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')


def search_books(request):
    query = request.GET.get('q', '')  # Get the search query
    books = BooksModel.objects.filter(title__icontains=query) if query else []  # Search books by title

    return render(request, 'search_results.html', {'books': books, 'query': query})

def order_history(request):
    orders = OrderModel.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "order_history.html", {"orders": orders})
