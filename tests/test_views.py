from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items,many=True)
        items_view = MenuItemView()
        self.assertEqual(serialized_items,items_view)
