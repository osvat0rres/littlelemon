from django.test import TestCase
from restaurant.models import Menu
from .views import MenuItemsView
from .serializer import MenuSerializer



class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Tittle="Ice cream", Price=10.99, Inventory = 100)
        self.assertEqual(str(item), "Ice cream : 10.99")
        
class MenuItemViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(
            Tittle = "Tv", 
            Price = 500.00,
            Inventory =  5   
        )
        
        Menu.objects.create(
            Tittle = "chair", 
            Price = 20.00 ,
            Inventory =  3  
        )
    
    def test_getall(self):
        response = self.client.get("/menu/")
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
        
        