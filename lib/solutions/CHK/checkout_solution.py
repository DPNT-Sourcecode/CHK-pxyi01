from collections import Counter
#from lib.solutions.CHK.items import *
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    tag_counts = Counter(skus)
    print(tag_counts)
    # items_list = [ItemA(), ItemB(), ItemC(), ItemD(), ItemE()]
    total_price = 0

    # for tag, count in tag_counts.items():
    #     item = next((item for item in items_list if item.tag == tag), None)

    #     if item is None:
    #         return -1
        
    #     print(item)
    #     total_price += item.calculate_cost(dict(tag_counts.items()))
    #     print (total_price)
    return total_price


