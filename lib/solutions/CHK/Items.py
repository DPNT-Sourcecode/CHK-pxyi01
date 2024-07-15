class ItemA:

    def __init__(self) -> None:
        self.item = "A"
        self.price = 50
        self.three_offer = 130
        self.five_offer = 200
    
    def calculate_cost(self, items_count) -> int:
        a_count = items_count[self.item]
        cost = 0

        cost += a_count // 5 * self.five_offer
        a_count %= 5
        cost += a_count // 3 * self.three_offer
        a_count %= 3
        return cost *= 
    


