from lib.solutions.CHK.checkout_solution import checkout
from lib.solutions.CHK.items import *

class TestCheckout():

    def test_total_price(self):
        assert checkout("AABCD") == 165
        assert checkout("AAABCD") == 195
        assert checkout("AAAABBBCCD") == 310
        assert checkout("AABBG") == -1
    
    def test_ItemA_class(self):
        item_counts = {"A" : 2}
        item = ItemA()
        cost = item.calculate_cost(item_counts)
        assert cost == 100
