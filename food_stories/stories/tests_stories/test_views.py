from django.test import TestCase
from stories.views import ContactView
from stories.forms import ContactForm
from stories.models import Contact
from django.urls import reverse_lazy

class ContactViewTestCase(TestCase):

    def setUp(self):
        self.contact_url = '/contact/'
        self.url = reverse_lazy('contact')
        self.view = ContactView()
        self.valid_data = {
            'name': 'Idris',
            'email': 'idris.sabanli@gmail.com',
            'phone_number': '+994551234567',
            'subject': 'Sayt islemir',
            'message': 'https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django bu unvanda problem var',
        }
        self.invalid_data = {
            'name': 'IdrisIdrisIdrisIdrisIdrisIdrisIdrisIdrisIdris',
            'email': 'idris.sabanli',
            'phone_number': '+994551234567',
            'subject': 'Sayt islemir',
            'message': 'https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django bu unvanda problem var',
        }
        
    
    def test_reverse_url(self):
        self.assertEqual(self.contact_url, self.url)

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertTemplateUsed(response, 'contact.html')

    def test_post_request(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        contact_data = Contact.objects.last()
        self.assertEqual(self.valid_data['name'], contact_data.name)
        self.assertEqual(self.valid_data['email'], contact_data.email)
        # self.assertEqual(self.valid_data['phone_number'], contact_data['phone_number'])
        self.assertEqual(self.valid_data['message'], contact_data.message)
        # self.assertIn('form', response.context)
        self.assertRedirects(response, '/')
    
    def test_post_invalid_request(self):
        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ensure this value has at most 40 characters (it has 45).", html=True)
