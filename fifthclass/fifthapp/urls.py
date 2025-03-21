from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('index', views.indexview,name='index'),
    path('about', views.AboutView, name='about'),
    path('category', views.CategoryView, name='category'),
    path('categoryadd', views.CategoryAdd, name='categoryadd'),
    path('categorydisplay', views.CategoryDisplay, name='categorydisplay'),
    path('categoryedit/<int:id>/', views.CategoryEdit, name='categoryedit'),
    path('categorydelete/<int:id>/', views.CategoryDelete, name='categorydelete'),
    path('categorydetails/<int:id>/', views.CategoryDetailsView, name='categorydetails'),

    # path('books', views.BooksView, name='books'),
    path('booksadd', views.BooksAdd, name='booksadd'),
    path('booksdisplay', views.BooksDisplay, name='booksdisplay'),
    path('booksedit/<int:id>/', views.BooksEdit, name='booksedit'),
    path('booksdelete/<int:id>/', views.BooksDelete, name='booksdelete'),
    path('booksingle/<int:id>/', views.BooksSingleDisplay, name='booksingle'),

    path('articles', views.ArticlesView, name='articles'),
    path('articlesadd', views.ArticlesAdd, name='articlesadd'),
    path('articlesdisplay', views.ArticlesDisplay, name='articlesdisplay'),
    path('articlesedit/<int:id>/', views.ArticlesEdit, name='articlesedit'),
    path('articlesdelete/<int:id>/',views.ArticlesDelete,name='articlesdelete'),
    path('articlesingle/<int:id>/', views.ArticlesSingleDisplay, name='articlesingle'),
    path('articlesdetails/<int:id>/', views.ArticleDetails, name='articlesdetails'),
    path('offers', views.OffersView, name='offers'),
    path('bookindividual/<int:id>/', views.BookIndividualView, name='bookindividual'),
    path('bestsellers',views.BestSellersView, name='bestsellers'),
    path('careers', views.CareersView, name='careers'),
    path('contactus', views.ContactUsView, name='contactus'),
    path('privacypolicy', views.PrivacyPolicyView, name='privacypolicy'),
    path('shipping&returns', views.ShippingandReturnsView, name='shipping&returns'),
    path('payments&refund', views.PaymentsandRefundView, name='payments&refund'),
    path('t&c', views.TandCView, name='t&c'),
    path('thankyou', views.ThankYouView, name='thankyou'),

    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-wishlist/<int:book_id>/',views.add_to_wishlist, name='add_to_wishlist'),
    path('book-list', views.BookListView, name='book_list'),

    path('cart', views.cart_view, name='cart'),
    path('wishlist', views.wishlist_view, name='wishlist'),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('move-to-wishlist/<int:item_id>/', views.move_to_wishlist, name='move_to_wishlist'),
    path('move-to-cart/<int:item_id>/', views.move_to_cart, name='move_to_cart'),

    path('checkout', views.checkout, name='checkout'),  # For cart-based purchases
    path('place_order', views.place_order, name='place_order'),
    path('cartbookindividual/<int:id>/', views.CartBookIndividual, name='cartbookindividual'),
    path('wishlistbookindividual/<int:id>/', views.WishlistBookIndividual, name='wishlistbookindividual'),
    path('order-success', views.order_success, name='order_success'),
    path('search/', views.search_books, name='search_books'),
    path("order-history/", views.order_history, name="order_history"),


    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),




]


