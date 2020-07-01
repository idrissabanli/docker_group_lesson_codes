from django.contrib import admin
from stories.models import Recipe, Tag, Category


admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Category)