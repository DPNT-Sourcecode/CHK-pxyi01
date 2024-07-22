from collections import Counter

class Shopping():

    def __init__(self):
        self.items = []
        self.item_counts = Counter()
    
    def calculate_total_cost(self):
        total_cost = 0

        for item in self.items:
            total_cost += item.cost
        
        return total_cost

    def add_item(self, item):
        self.items.append(item)
        self.item_counts[item.tag] += 1

class Offer():

    def apply_discount(self, item, item_count):

    

class Item():

    def __init__(self, tag, cost) -> None:
        self.tag = tag
        self.cost = cost
            

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





