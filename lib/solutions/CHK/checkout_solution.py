from collections import Counter
from Items import *
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    tag_counts = Counter(skus)
    items_list = [ItemA(), ItemB(), ItemC(), ItemD(), ItemE()]
    total_price = 0

    for tag, count in tag_counts:
        item = next((item for item in items_list))
        try:
            total_price += price_map[item]
        except:
            return -1
        

    return total_price




