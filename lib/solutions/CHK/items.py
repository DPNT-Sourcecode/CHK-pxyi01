import math

class Shopping():

    def __init__(self):
        self.items = []
    
    def calculate_total_cost(self):
        total_cost = 0
    
        self.apply_offers()
        total_cost += self.apply_discounts()
        total_cost += self.add_item_prices()

        return total_cost

    def add_item(self, item):
        self.items.append(item)
    
    def apply_offers(self):
        for item in self.items:
            Offer.apply_buyfree_offer(item, self.items)
    
    def apply_discounts(self):
        cost = 0

        for item in self.items:
            cost += Offer.get_discounted_cost(item)
        
        return cost

    def add_item_prices(self):
        cost = 0

        for item in self.items:
            cost += item.cost * item.count

        return cost

class Offer():

    @staticmethod
    def get_discounted_cost(item):
        discounted_cost = 0

        if item.tag == "A":
            discounted_cost += Offer.get_discounted_cost_helper(item, 5, 200)
            discounted_cost += Offer.get_discounted_cost_helper(item, 3, 130)
        
        elif item.tag == "B":
            discounted_cost += Offer.get_discounted_cost_helper(item, 2, 45)
        
        elif item.tag == "H":
            discounted_cost += Offer.get_discounted_cost_helper(item, 10, 80)
            discounted_cost += Offer.get_discounted_cost_helper(item, 5, 45)

        elif item.tag == "K":
            discounted_cost += Offer.get_discounted_cost_helper(item, 2, 150)

        elif item.tag == "P":
            discounted_cost += Offer.get_discounted_cost_helper(item, 5, 200)

        elif item.tag == "Q":
            discounted_cost += Offer.get_discounted_cost_helper(item, 3, 80)

        elif item.tag == "V":
            discounted_cost += Offer.get_discounted_cost_helper(item, 3, 130)
            discounted_cost += Offer.get_discounted_cost_helper(item, 2, 90)

        return discounted_cost
    
    def get_discounted_cost_helper(item, buys_needed, discount):
        discounted_cost = item.count // buys_needed * discount
        item.count %= buys_needed
        return discounted_cost
    
    @staticmethod
    def apply_buyfree_offer(item, items):
        if item.tag == "E":
            Offer.buyfree_helper(item, items, 2, "B")
        
        elif item.tag == "N":
            Offer.buyfree_helper(item, items, 3, "M")

        elif item.tag == "R":
            Offer.buyfree_helper(item, items, 3, "Q")
        
        if item.tag == "F":
            Offer.buyownfree_helper(item, 2)

        elif item.tag == "U":
            Offer.buyownfree_helper(item, 3)
    
    def buyfree_helper(item, items, buys_needed, free_item_tag):
        free_items = item.count // buys_needed
        matched_item = next(filter(lambda x: x.tag == free_item_tag, items), None)

        if matched_item is not None:
            matched_item.count -= free_items
            matched_item.count = 0 if matched_item.count < 0 else matched_item.count
    
    def buyownfree_helper(item, buys_needed):
        effective_item_count = 0

        while (item.count > buys_needed):
            item.count -= buys_needed
            effective_item_count += 1
        
        item.count = effective_item_count + item.count

class Item():

    def __init__(self, tag, cost, count) -> None:
        self.tag = tag
        self.cost = cost
        self.count = count
            




