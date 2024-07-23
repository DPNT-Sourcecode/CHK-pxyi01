class Shopping():

    def __init__(self):
        self.items = []
    
    def calculate_total_cost(self):
        total_cost = 0
        print("new execution")
        for item in self.items:
            print(f"item {item.tag}")
            Offer.apply_buyfree_offer(item, self.items)
            total_cost += Offer.get_discounted_cost(item)
            total_cost += item.cost * item.count
            print(f"total cost: {total_cost}")
            print("==============")
        return total_cost

    def add_item(self, item):
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
        
        elif item.tag == "B":
            discounted_cost += item.count // 2 * 45
            item.count %= 2 

        return discounted_cost
    
    
    @staticmethod
    def apply_buyfree_offer(item, items):
        if item.tag == "E":
            free_Bs = item.count // 2
            matched_item = next(filter(lambda x: x.tag == "B", items), None)

            if matched_item is not None:
                matched_item.count -= free_Bs
                matched_item.count = 0 if matched_item.count < 0 else matched_item.count

class Item():

    def __init__(self, tag, cost, count) -> None:
        self.tag = tag
        self.cost = cost
        self.count = count
            






