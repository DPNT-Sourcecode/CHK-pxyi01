from collections import Counter
from Items import *
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_counts = Counter(skus)
    items = [ItemA(), ItemB(), ItemC(), ItemD(), ItemE()]
    total_price = 0

    for item in skus:
        try:
            total_price += price_map[item]
        except:
            return -1
        #item_counts[item] += 1

        if item == "A":
            a_count += 1
        
        if item == "B":
            b_count += 1
        
        if a_count == 3:
            total_price -= 20 # 20 is discounted when 3 A's are bought
            a_count = 0

        if b_count == 2:
            total_price -= 15 # 15 is discounted when 2 B's are bought
            b_count = 0

    return total_price

def apply_discount(item_counts):
    for item, count in item_counts:
        if count == discount_item_count[item]:
            pass
