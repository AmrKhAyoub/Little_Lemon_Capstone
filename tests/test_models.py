from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='fanta',price=7,inventory=70)
        itemstr = item.get_item()
        self.assertEqual(itemstr,'fanta : 7')
        
