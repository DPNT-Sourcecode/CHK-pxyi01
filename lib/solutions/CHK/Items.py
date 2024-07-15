from abc import ABC, abstractmethod

class Item(ABC):

    @abstractmethod
    def calculate_cost(self, items_count) -> int:
        pass
        

class ItemA(Item):

    def __init__(self) -> None:
        self.item = "A"
        self.price = 50
    
    def calculate_cost(self, items_count) -> int:
        count = items_count[self.item]
        cost = 0

        cost += self.apply_discount(130, 3, count)
        cost += self.apply_discount(200, 5, count)
        cost += count * self.price
        return cost
    
    def apply_discount(self, discount, number_for_discount, item_count) -> int:
        cost = item_count // number_for_discount * discount
        item_count %= number_for_discount
        return cost
    
class ItemB(Item):

    def __init__(self) -> None:
        self.item_for_discount = "E"
        self.item = "B"
        self.price = 30
    
    def calculate_cost(self, items_count) -> int:
        count = items_count[self.item]
        e_count = items_count[self.item_for_discount]
        cost = 0

        count -= e_count // 2
        cost += self.apply_discount(45, 2, count)
        cost += count * self.price
        return cost

    def apply_discount(self, discount, number_for_discount, item_count) -> int:
        cost = item_count // number_for_discount * discount
        item_count %= number_for_discount
        return cost

class ItemC(Item):

    def __init__(self) -> None:
        self.item = "C"
        self.price = 50
    
    def calculate_cost(self, items_count) -> int:
        count = items_count[self.item]
        cost = 0

        cost += count * self.price
        return cost

class ItemD(Item):

    def __init__(self) -> None:
        self.item = "D"
        self.price = 15

    def calculate_cost(self, items_count) -> int:
        a_count = items_count[self.item]
        cost = 0

        cost += a_count * self.price
        return cost

class ItemE(Item):

    def __init__(self) -> None:
        self.item = "E"
        self.price = 40
    
    def calculate_cost(self, items_count) -> int:
        a_count = items_count[self.item]
        cost = 0

        cost += a_count * self.price
        return cost





