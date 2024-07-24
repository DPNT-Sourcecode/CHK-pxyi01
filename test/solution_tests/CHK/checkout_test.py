from lib.solutions.CHK.checkout_solution import checkout

class TestCheckout():

    def test_total_price(self):
        assert checkout("AABCD") == 165
        assert checkout("AAABCD") == 195
        assert checkout("AAAABBBCCD") == 310
        assert checkout("AABBG") == 165
        assert checkout("BBEE") == 110
        assert checkout("BBE") == 85
        assert checkout("AAAAAAA") == 300
        assert checkout("FFFFFFF") == 40
        assert checkout("FFFFFF") == 40
        assert checkout("FF") == 20
        assert checkout("FFF") == 20
        assert checkout("FFFF") == 30
        assert checkout("ABCFFFF") == 130
        assert checkout("UUU") == 120
        assert checkout("UU") == 80
        assert checkout("UUUU") == 120
        assert checkout("UUUUUUUU") == 240
        assert checkout("VVVVRRQR") == 330
        assert checkout ("SSA") == 90



