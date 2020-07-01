from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

USER_MODEL = get_user_model()


class Category(models.Model):
    """
    Bu model reseptlerin ve storilerin kategoriyalarini saxlamaq ucundu.
    Misal: Deset, Yemek
    """

    #informations
    title = models.CharField('Title', max_length=120)
    image = models.ImageField('Image', upload_to='category_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    order = models.PositiveIntegerField('Order', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('order',)
    
    def __str__(self):
        return self.title


class Tag(models.Model):

    #information
    title = models.CharField('Title', max_length=40)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'
    
    def __str__(self):
        return self.title


class Recipe(models.Model):
    # relations
    category = models.ForeignKey(Category, verbose_name='Kateqoriya', on_delete=models.CASCADE, db_index=True, related_name='recipes')
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='recipes')
    author = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, db_index=True, related_name='recipes')

    # informations
    title = models.CharField('Basligi', max_length=120)
    short_description = models.CharField('Qisa Mezmunu', max_length=255, help_text='Bu sahe repestler siyahisinda reseptin mezmunu olaraq gorunur...')
    image = models.ImageField('Sekil', upload_to='recipes')
    long_description = models.TextField('Genis mezmunu')
    # author = models.CharField('Muellif', max_length=50)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta: # table name: stroies_recipe
        # app_label = 'story'
        # db_table = 'resept'
        verbose_name = 'Resept'
        verbose_name_plural = 'Reseptler'
        ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.title} category: {self.category}"


class Comment(models.Model):
    # relations
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    # story to do add story model and relation here
    user = models.ForeignKey(USER_MODEL, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    parent_comment = models.ForeignKey('self', related_name='child_comments', on_delete=models.CASCADE, null=True, blank=True)

    user_name = models.CharField('Name', max_length=50, null=True, blank=True)
    email = models.EmailField('Email', max_length=40, null=True, blank=True)
    # website = models.URLField('Website', null=True, blank=True)
    message = models.TextField('Message')


"""
|id | message | parent_id |
| 1 | Eladi | null |
| 2 | Chsdnfklsdf | 1 |
| 3 | Chsdnfklsdf | 1 |
| 4 | Chsdnfklsdf | null |
| 5 | Chsdnfklsdf | 2 |
"""

# 1,       4 
# 2, 3     []
# 5, []

