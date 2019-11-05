from django import forms
from .validators.form_validators import *
from .models import Book, Comment

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=20, label="Kitabin Basligi", widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    class Meta:
        model = Book
        fields = '__all__'

    # def save(self):
    #     instance = super().save(commit=False)
    #     instance.title = instance.title.capitalize()
    #     instance.price = instance.price + (instance.price *10)/100
    #     instance.save()
    #     return instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]


