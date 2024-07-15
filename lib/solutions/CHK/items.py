from abc import ABC, abstractmethod

class Item(ABC):

    @abstractmethod
    def calculate_cost(self, items_count) -> int:
        pass
        

class ItemA(Item):

    def __init__(self) -> None:
        self.tag = "A"
        self.price = 50
    
    def calculate_cost(self, items_count) -> int:
        self.count = items_count[self.tag]
        cost = 0

        cost += self.apply_discount(130, 3)
        cost += self.apply_discount(200, 5)
        cost += self.count * self.price
        return cost
    
    def apply_discount(self, discount, number_for_discount) -> int:
        cost = self.count // number_for_discount * discount
        self.count %= number_for_discount
        return cost
    
class ItemB(Item):

    def __init__(self) -> None:
        self.tag_for_discount = "E"
        self.tag = "B"
        self.price = 30
    
    def calculate_cost(self, items_count) -> int:
        self.count = items_count[self.tag]
        e_count = items_count.get(self.tag_for_discount, 0)
        cost = 0

        self.count -= e_count // 2
        cost += self.apply_discount(45, 2)
        cost += self.count * self.price
        return cost

    def apply_discount(self, discount, number_for_discount) -> int:
        cost = self.count // number_for_discount * discount
        self.count %= number_for_discount
        return cost

class ItemC(Item):

    def __init__(self) -> None:
        self.tag = "C"
        self.price = 20
    
    def calculate_cost(self, items_count) -> int:
        self.count = items_count[self.tag]
        cost = 0

        cost += self.count * self.price
        return cost

class ItemD(Item):

    def __init__(self) -> None:
        self.tag = "D"
        self.price = 15

    def calculate_cost(self, items_count) -> int:
        a_count = items_count[self.tag]
        cost = 0

        cost += a_count * self.price
        return cost

class ItemE(Item):

    def __init__(self) -> None:
        self.tag = "E"
        self.price = 40
    
    def calculate_cost(self, items_count) -> int:
        a_count = items_count[self.tag]
        cost = 0

        cost += a_count * self.price
        return cost
