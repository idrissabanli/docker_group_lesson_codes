from django.test import TestCase
from django.template import Template, Context
from stories.models import Category


class GetCategoriesTagTaseCase(TestCase):
    
    def setUp(self):
        html = """
        {% load custom_tags %}
        {% get_categories as categories %}

        {% for category in categories %}
        <h1>{{category.title}}</h1>
        {% endfor %}
        """
        context = {
        }
        context = Context(context)
        self.content = Template(html).render(context)
        self.categories = Category.objects.all()[:3]

    def test_categories(self):
        for cat in self.categories:
            self.assertIn(cat.title, self.content)


class UpperTemplateFilterTeseCase(TestCase):

    def setUp(self):
        context = {
            'name': 'samir'
        }
        context = Context(context)
        html = """
        <h1>{{ name|upper }}</h1>
        """
        self.content = Template(html).render(context)
    
    def test_upper(self):
        self.assertIn("SAMIR", self.content)
