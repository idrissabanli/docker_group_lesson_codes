from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # print(request.GET)
    full_name = request.GET.get('full_name')
    context = {
        'full_name': full_name,
        'title': 'tech academy',
        'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident expedita hic enim delectus, pariatur non ea error! Maxime, quidem nemo at vel natus iure numquam! Nemo recusandae facilis sint aspernatur?',
        'html': '<h1>Welcome</h1>',
        'array': [1,2,3,4,5,6],
        'pi': 3.14572
    }
    return render(request, 'index.html', context)

def main(request):
    html = '<h1>Salam Dunya</h1>'
    return HttpResponse(html)

def template_custom(request):
    context = {
        'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident expedita hic enim delectus, pariatur non ea error! Maxime, quidem nemo at vel natus iure numquam! Nemo recusandae facilis sint aspernatur?',
    }
    return render(request, 'template_custom.html', context)


    

# @core.router('/')
# def home():
#     return