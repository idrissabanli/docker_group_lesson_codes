from django.db import models


class Recipe(models.Model):
    title = models.CharField('Basligi', max_length=120)
    category = models.IntegerField('Kateqoriya', choices=((1, 'Dessert'), (2, 'Food')))
    short_description = models.CharField('Qisa Mezmunu', max_length=255, help_text='Bu sahe repestler siyahisinda reseptin mezmunu olaraq gorunur...')
    image = models.ImageField('Sekil', upload_to='media/recipes')
    long_description = models.TextField('Genis mezmunu')
    author = models.CharField('Muellif', max_length=50)

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
        return f"{self.title} category: {self.get_category_display()}"


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('cg', 'Convenience Goods'),
        ('shg', 'Shopping Goods'),
        ('sg', 'Specialty Goods'),
    )
    name = models.CharField(max_length=125, unique=True)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES )
    picture = models.ImageField(upload_to='media/products/images/')
    amount = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)
    production_date  = models.DateTimeField(auto_now_add=True, editable=True)
    is_new = models.BooleanField(default=False)
    certificate = models.FileField(upload_to='media/products/files/', null=True, blank=True)
    rating = models.DecimalField(default=0.0, max_digits=2, decimal_places=1, null=True, blank=True)
    detailed_view_link = models.URLField(null=True, blank=True, max_length=300)


