from collections import Counter
from lib.solutions.CHK.items import *

# noinspection PyUnusedLocal
# skus = unicode string
item_costs = {
    "A": 50, 
    "B": 30, 
    "C": 20, 
    "D": 15, 
    "E": 40, 
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21
    }

def checkout(skus):
    item_counts = Counter(skus)
    shopping = Shopping()

    for tag, count in item_counts.items():
        item_cost = item_costs.get(tag)

        if item_cost is None:
            return -1
        
        item = Item(tag, item_cost, count)
        shopping.add_item(item)
    
    total_price = shopping.calculate_total_cost()
    return total_price


