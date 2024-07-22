from collections import Counter
from items import *
#from lib.solutions.CHK.items import *
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_counts = Counter(skus)
    shopping = Shopping()

    for tag, count in item_counts.items():
        item = Item(tag, count)
    return total_price



