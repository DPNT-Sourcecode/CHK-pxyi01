from lib.solutions.CHK import checkout_solution

class TestCheckout():

    def test_total_price(self):
        assert checkout_solution("AABCD") == 165