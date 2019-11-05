from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'model_app'

urlpatterns = [
    # path('create-book/', CreateBook.as_view(), name='create_book'), 
    path('books/', books, name='books'),
    path('get_form/', form_view, name='form_view'), 
    path('welcome/', TemplateView.as_view(template_name='template_view.html'), name='welcome'),
    path('bloggers/', BookList.as_view(), name='bloggers'),
    path('blogger/<int:pk>/', BloggerDetail.as_view(), name='blogger'),
    path('create-blogger/', CreateBlogger.as_view(), name="create-blogger"),
    path('update-blogger/<int:pk>/', UpdateBlogger.as_view(), name="update-blogger"),
    path('delete-blogger/<int:pk>/', DeleteBlogger.as_view(), name="delete-blogger"),
    path('form-book/', BookMyFormView.as_view(), name="form-blogger"),
]
