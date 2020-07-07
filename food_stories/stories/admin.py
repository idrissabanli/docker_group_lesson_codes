from django.contrib import admin
from stories.models import Recipe, Tag, Category, Contact
from stories.forms import RecipeAdminForm


class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('title', 'category', 'author', 'created_at', 'is_published',)
    search_fields = ('title', 'category__title', 'author__first_name', 'author__last_name', 'author__username')
    list_filter = ('title', 'category__title', 'author__username', 'created_at',)
    # fields = ('title', 'category', 'author', 'tags', 'short_description', 'long_description', 'image', 'is_published',)
    save_on_top = True
    fieldsets = (
        ('Information', {
            'description': 'bu saheler melumat xarakterlidir',
            'classes': ('collapse',),
            'fields': ('title', 'short_description', 'long_description', 'image',)
        }),
        ('relations', {
            'description': 'relations desc',
            'classes': ('collapse',),
            'fields': ('category', 'author', 'tags',)
        }),
        ('moderation', {
            'description': 'moderation desc',
            'classes': ('collapse',),
            'fields': ('is_published',)
        }),
    )
   

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Contact)