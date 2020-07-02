from django.shortcuts import render
from main.models import Book, Category
from django.db.models import Q
from django.contrib import messages

def book_list(request):
    books = Book.objects.filter(is_published=True)
    search_word = request.GET.get('search', '')
    category = request.GET.get('category', 0)
    if not isinstance(category, int) and not category.isdigit():
        messages.error(request, 'Category reqem daxil edilmelidir')
        category = 0
    categories = Category.objects.all()
    print(search_word)
    if search_word:
        books = books.filter(Q(title__icontains=search_word) | Q(author__fullname__icontains=search_word))
    if category != '0' and category != 0:
        books = books.filter(category__id=category)
    context = {
        'books': books,
        'categories': categories,
        'searched_category': int(category),
        'search_word': search_word
    }
    return render(request, 'book_list.html', context)