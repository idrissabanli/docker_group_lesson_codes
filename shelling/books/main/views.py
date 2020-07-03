import math

from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages

from main.models import Book, Category

def book_list(request):
    context = {}
    query_dict = {
        'is_published': True
    }
    page = request.GET.get('page', 1)
    search_query = request.get_full_path()
    print(search_query)

    if isinstance(page, str) and page.isdigit():
        page = int(page)

    books = Book.objects.filter()
    search_word = request.GET.get('search', '')
    category = request.GET.get('category', 0)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price is not None and min_price.isdigit():
        context['min_price'] = min_price
        query_dict['price__gte'] = float(min_price)

    if max_price is not None and max_price.isdigit():
        context['max_price'] = max_price
        query_dict['price__lte'] = float(max_price)

    if not isinstance(category, int) and not category.isdigit():
        messages.error(request, 'Category reqem daxil edilmelidir')
        category = 0
        
    if category != '0' and category != 0:
        context['searched_category']= int(category)
        query_dict['category__id'] = category
    

    books = Book.objects.filter(**query_dict)
    if search_word:
        context['search_word'] = search_word
        books = books.filter(Q(title__icontains=search_word) | Q(author__fullname__icontains=search_word))
    
    # page 1 = [0,2]
    # 2 = [2, 4]
    # 3 [4,6]
    book_count = books.count()
    books = books[(page-1)*2: page*2]
    print(book_count)
    book_size_for_per_page = 2
    page_count = math.ceil(book_count/book_size_for_per_page)
    print()
    page_range = range(1, page_count+1)

    print(search_word)

    categories = Category.objects.all()
    print(search_word)
    context = {**context, **{
        'books': books,
        'categories': categories,
        'page_count': page_count,
        'page_range': page_range,
        'current_page_number': page,
        'previous_page': page - 1,
        'next_page': page + 1,
        'search_query': search_query
        }}
    return render(request, 'book_list.html', context)