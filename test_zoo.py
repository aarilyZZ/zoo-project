import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_child_ticket_(self):
        self.assertEqual(self.zoo.get_ticket_price(8), 50)
    
    def test_teenage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_teenage_price(self):
        self.assertEqual(self.zoo.get_ticket_price(16), 100)
    
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test_adult_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_grans_price(self):
        self.assertEqual(self.zoo.get_ticket_price(68), 100)
    
    def test_invalid(self):
        self.assertEqual(self.zoo.get_ticket_price(-8), "Invalid Age")

    def test_invalid_2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

if __name__ == '__main__':
    unittest.main()