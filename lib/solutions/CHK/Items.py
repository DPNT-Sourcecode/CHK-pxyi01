from abc import ABC, abstractmethod

class Item(ABC):

    @abstractmethod
    def calculate_cost(self, items_count) -> int:
        pass

class ItemA(Item):

    def __init__(self) -> None:
        self.item = "A"
        self.price = 50
        self.three_offer = 130
        self.five_offer = 200
    
    def calculate_cost(self, items_count) -> int:
        count = items_count[self.item]
        cost = 0

        cost += count // 5 * self.five_offer
        count %= 5
        cost += count // 3 * self.three_offer
        count %= 3
        cost += count * self.price
        return cost
    
    def apply_discount(self, offer, count)
    
class ItemB(Item):

    def __init__(self) -> None:
        self.item = "B"
        self.price = 30
        self.two_offer_price = 45
    
    def calculate_cost(self, items_count) -> int:
        count = items_count[self.item]
        cost = 0

        cost += count // 2 * self.two_offer
        count %= 2
        cost += count * self.price
        return cost


class ItemC(Item):

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
        cost += a_count * self.price
        return cost

class ItemD(Item):

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
        cost += a_count * self.price
        return cost

class ItemE(Item):

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
        cost += a_count * self.price
        return cost



