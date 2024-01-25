from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="IceCream-1", price=81, inventory=101)
        Menu.objects.create(title="IceCream-2", price=82, inventory=102)
        Menu.objects.create(title="IceCream-3", price=83, inventory=103)
        Menu.objects.create(title="IceCream-4", price=84, inventory=104)

    def test_getall(self):
        resp = self.client.get("/restaurant/menu/")
        self.assertEqual(resp.status_code, 200)
        data = resp.json().get("results")
        for m in data:
            serializer = MenuSerializer(data=m)
            self.assertTrue(serializer.is_valid())
