from collections import Counter
from Items import *
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_counts = Counter(skus)
    items = [ItemA(), ItemB(), ItemC(), ItemD(), ItemE()]
    total_price = 0

    for item, count in item_counts:
        
        try:
            total_price += price_map[item]
        except:
            return -1
        

    return total_price



