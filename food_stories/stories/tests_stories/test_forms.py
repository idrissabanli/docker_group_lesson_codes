from django.test import TestCase
from stories.forms import ContactForm


class ContactFormTestCase(TestCase):

    def setUp(self):
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
        self.invalid_data2 = {
            'name': 'IdrisIdrisIdrisIdrisIdrisIdrisIdrisIdrisIdris',
            'email': 'idris.sabanli',
            'phone_number': '+9945512345674334',
            'subject': 'Sayt islemir',
            'message': 'https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django bu unvanda problem var',
        }
        self.invalid_data3 = {
            'name': 'Idris',
            'email': 'idris.sabanli@gmail.com',
            'phone_number': '+994551234567',
        }
    
    def test_valid_data(self):
        form  = ContactForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_data(self):
        form  = ContactForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('name', form.errors.keys())
        self.assertIn('Ensure this value has at most 40 characters (it has 45).', form.errors['name'])
        
    def test_invalid_data2(self):
        form  = ContactForm(data=self.invalid_data2)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('phone_number', form.errors.keys())
        self.assertIn('Ensure this value has at most 13 characters (it has 17).', form.errors['phone_number'])
    
    def test_invalid_data3(self):
        form  = ContactForm(data=self.invalid_data3)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('subject', form.errors.keys())
        self.assertIn('message', form.errors.keys())
        