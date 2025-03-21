from django import forms

from fifthapp.models import ArticlesModel, OffersModel, BooksModel, CategoryModel, CartModel, WishlistModel


class CategoryForm(forms.ModelForm):
    class Meta:
        model=CategoryModel
        fields='__all__'

class BooksForm(forms.ModelForm):
    class Meta:
        model=BooksModel
        fields='__all__'

class ArticlesForm(forms.ModelForm):
    class Meta:
        model=ArticlesModel
        fields='__all__'

class OffersForm(forms.ModelForm):
    class Meta:
        model=OffersModel
        fields='__all__'

class CartForm(forms.ModelForm):
    class Meta:
        model=CartModel
        fields='__all__'

class WishlistForm(forms.ModelForm):
    class Meta:
        model=WishlistModel
        fields='__all__'
