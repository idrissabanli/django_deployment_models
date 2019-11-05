from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.views.generic.edit import FormMixin
from django.core.paginator import Paginator
from .forms import BookForm, CommentForm
# Create your views here.

# class CreateBook(CreateView):
#     model = Book
#     template_name = 'book_form.html'
#     success_url = reverse_lazy('core_app:create_book') # returned /create-book/

from django.db.models import Q, F
def books(request):
    book_list = Book.objects.filter(Q(page_count__lt=500) | Q(price__lt=F('page_count')/100))
    print(book_list.query)
    paginator = Paginator(book_list, 2) 
    page = request.GET.get('page', 1)
    books = paginator.get_page(page)
    print(books)
    context = {
        'books':books,
    }
    return render(request, 'books.html', context)

def form_view(request):
    form = BookForm()
    context = {}
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context['myform']= form
    return render(request, 'form_example.html', context)

class BookList(ListView):
    model = Blogger
    template_name = 'listview.html'
    context_object_name = 'kitablar'
    paginate_by = 5

    # def get_queryset(self):
    #     return Book.objects.values('title')

class BloggerDetail(FormMixin, DetailView):
    model = Blogger
    form_class = CommentForm
    template_name = 'blogger_detail.html'
    context_object_name = 'person'

    def get_success_url(self):
        return reverse_lazy('model_app:blogger', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return super().form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.blogger = self.object
        comment.save()
        return super().form_valid(form)


class CreateBlogger(CreateView):
    model = Blogger
    template_name = 'blogger_create.html'
    fields = '__all__'

class UpdateBlogger(UpdateView):
    model = Blogger
    template_name = 'blogger_create.html'
    fields = '__all__'


class DeleteBlogger(DeleteView):
    model = Blogger
    template_name = 'delete_blogger.html'
    success_url = reverse_lazy('model_app:bloggers')

class BookMyFormView(FormView):
    form_class = BookForm
    template_name = 'book_my_form.html'
    success_url = reverse_lazy('model_app:bloggers')


    