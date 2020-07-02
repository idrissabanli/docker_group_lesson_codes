from django.db import models
from django.contrib.auth import get_user_model



class Author(models.Model):

    #information
    gender_choice = [
        ('mr', 'man'),
        ('ms', 'woman'),
    ]
    fullname = models.CharField('Name',max_length=255)
    image = models.ImageField('Image',upload_to = 'media/author_images')
    gender = models.CharField('Gender',max_length=2,choices=gender_choice)
    date_of_birthday= models.DateField('Date of birth')
    nationality = models.CharField('Nationality',max_length=255)
    info = models.TextField('Info')

    def __str__(self):
        return self.fullname



class Book(models.Model):
    #relations
    author = models.ForeignKey(Author,verbose_name='Author',on_delete=models.CASCADE,db_index=True,related_name='recipes')
    category = models.ManyToManyField('Category', verbose_name='Categories', related_name='books')

    #information
    title = models.CharField('Title',max_length=120)
    image = models.ImageField('Image',upload_to = 'media/category_images')
    description = models.TextField('Description')
    price = models.DecimalField('Price',max_digits=7,decimal_places=2)
    page_count = models.IntegerField('Pages')

    #moderations
    is_published = models.BooleanField('is published', default=True)
    order = models.PositiveIntegerField('Order',default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

    @property
    def categories(self):
        cats = self.category.values_list('title', flat=True)
        return ', '.join(cats)


class Category(models.Model):

    #information
    title = models.CharField('Title',max_length=255)

    def __str__(self):
        return self.title

