from django.db import models
from .file_folders import *
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

GENDERS = (
    ('k', "Kisi"),
    ('q', "Qadin"),
)

class Blogger(models.Model):
    name = models.CharField("Video bloggerin adi", help_text="Adinizi daxil edin", max_length=50)
    nickname = models.CharField("Nickname", max_length=20)
    avatar = models.ImageField(upload_to="blogger")
    gender = models.CharField('Cinsi', choices=GENDERS, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blogger"
        verbose_name_plural = "Bloggerler siyahisi"
        ordering = ("-nickname",)
        db_table = "bloggerler_siyahisi"

    def __str__(self):
        return self.name

    def get_videos(self):
        return self.blogger_videos.all()
    
    def get_absolute_url(self):
        return reverse_lazy('model_app:blogger', kwargs={'pk':self.pk})
  

class Video(models.Model):
    title = models.CharField('Videonun basligi', help_text="Videonun basligi buraya yazilmalidir...", max_length=20)
    description = models.TextField('Text field', blank=True)
    blogger = models.ForeignKey(Blogger, related_name="blogger_videos", on_delete=models.CASCADE)
    video_path = models.FileField(upload_to="video_files/", blank=True)
    cover = models.ImageField(upload_to="video_images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Author(models.Model):
    full_name = models.CharField('Full Adı', max_length=50)
    image = models.ImageField(upload_to='authors/',)
    gender = models.CharField('Cinsi', choices=GENDERS, max_length=1)
    date_of_birthday = models.DateField()
    nationality = models.CharField('Milliyeti', max_length=30)
    info = models.TextField('Yazici haqqinda')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Yazici"
        verbose_name_plural = "Yazicilar"

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(verbose_name="Kitabin Başlığı", max_length=255)
    description = models.TextField('Məzmun')
    author = models.ForeignKey(to=Author, related_name="author_books", verbose_name="Muellif", on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Qiymet', max_digits=5, decimal_places=2)
    page_count = models.IntegerField('Sehife sayi')
    cover_image = models.ImageField('Cover sekili', upload_to=book_image_folder)
    categories = models.ManyToManyField(Category, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kitab"
        verbose_name_plural = "Kitablar"
        ordering = 'page_count',

    def __str__(self):
        return self.title  

class Contact(models.Model):
    full_name = models.CharField('ad, Soyad', max_length=40)
    subject = models.CharField('Movzu', max_length=255)
    content = models.TextField('Mezmun',)
    email = models.EmailField(verbose_name="E poct", max_length=20, )

    def __str__(self):
        return '{:s} {:s}'.format(self.subject, self.email)


class Comment(models.Model):
    content = models.TextField('context')
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    blogger = models.ForeignKey(Blogger, related_name='commets', on_delete=models.CASCADE)

    def __str__(self):
        return self.content

        