from collections import Counter
from lib.solutions.CHK.items import *

# noinspection PyUnusedLocal
# skus = unicode string
item_costs = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

def checkout(skus):
    item_counts = Counter(skus)
    shopping = Shopping()

    for tag, count in item_counts.items():
        item_cost = item_costs.get(tag)
        item = Item(tag, item_cost, count)
        shopping.add_item(item)
    
    total_price = shopping.calculate_total_cost()
    return total_price



