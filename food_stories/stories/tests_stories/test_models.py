from django.test import TestCase
from stories.models import Contact


class ContactTestCase(TestCase):

    def setUp(self):
        self.model_data = {
            'name': 'Idris',
            'email': 'idris.sabanli@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django bu unvanda problem var',
        }
        self.model_data2 = {
            'name': 'Amil',
            'email': 'amil@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django bu unvanda problem var',
        }
        self.content = Contact.objects.create(**self.model_data)
        self.content2 = Contact.objects.create(**self.model_data2)
    
    def test_created_data(self):
        contact_data = Contact.objects.all()[0]
        self.assertEqual(contact_data, self.content)
        contact_data = Contact.objects.all()[1]
        self.assertEqual(contact_data, self.content2)

    def test_str_method(self):
        expected_result = f"{self.content.name} subject: {self.content.subject}"
        self.assertEqual(expected_result, self.content.__str__())
        expected_result = f"{self.content2.name} subject: {self.content2.subject}"
        self.assertEqual(expected_result, self.content2.__str__())
    
    def test_get_email_method(self):
        expected_result = self.content.email
        self.assertEqual(expected_result, self.content.get_email())
        expected_result = self.content2.email
        self.assertEqual(expected_result, self.content2.get_email())

    def tearDown(self):
        Contact.objects.filter(id__in=[self.content.id, self.content2.id]).delete()