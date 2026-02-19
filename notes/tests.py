from django.test import TestCase
from .utils import add

# Create your tests here.

class AddTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
      
      
      
      
      
      
      
      
class NotesTestCase(TestCase):
    def test_note_can_be_added(self):
        response = self.client.post(reverse('notes:add'),{
            'title': 'Test Note',
            'description': 'This is a test note.'
        })
        self.assertEqual(response.status_code, 302)

        reshome = self.client.get(response.url)
        self.assertContains(reshome, "Test Note")  
        