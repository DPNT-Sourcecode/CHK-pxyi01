class Shopping():
    valid_tags = ["A", "B", "C", "D", "E"]

    def __init__(self):
        self.items = []
    
    def calculate_total_cost(self):
        total_cost = 0

        for item in self.items:
            total_cost += Offer.get_discounted_cost(item)
            total_cost += item.cost * item.count
        
        return total_cost

    def add_item(self, item):
        if item.tag not in Shopping.valid_tags:
            raise Exception("Not a valid item!")
        
        self.items.append(item)

class Offer():

    @staticmethod
    def get_discounted_cost(item):
        discounted_cost = 0

        if item.tag == "A":
            discounted_cost += item.count // 5 * 200
            item.count %= 5
            discounted_cost += item.count // 3 * 130
            item.count %= 3
            discounted_cost += item.count*item.cost
        
        elif item.tag == "B":
            discounted_cost += item.count // 2 * 45
            item.count %= 2
            discounted_cost += item.count*item.cost

        return discounted_cost

class Item():

    def __init__(self, tag, cost, count) -> None:
        self.tag = tag
        self.cost = cost
        self.count = count
            

