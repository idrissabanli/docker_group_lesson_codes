from django.contrib import admin
from stories.models import Recipe, Tag, Category, Contact


admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Contact)