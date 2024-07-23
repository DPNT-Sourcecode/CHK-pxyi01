from lib.solutions.CHK.checkout_solution import checkout

class TestCheckout():

    def test_total_price(self):
        assert checkout("AABCD") == 165
        assert checkout("AAABCD") == 195
        assert checkout("AAAABBBCCD") == 310
        assert checkout("AABBG") == -1
        assert checkout("BBEE") == 110
        assert checkout("BBE") == 85
        assert checkout("AAAAAAA") == 300
        assert checkout("FFFFFFF") == 40
        assert checkout("FFFFFF") == 40
        assert checkout("FF") == 20
        assert checkout ("FFF") == 20
        assert checkout ("FFFF") == 30
        assert checkout ("ABCFFFF") == 130


