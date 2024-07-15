from collections import Counter
import Items
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    tag_counts = Counter(skus)
    items_list = [ItemA(), ItemB(), ItemC(), ItemD(), ItemE()]
    total_price = 0

    for tag, count in tag_counts:
        item = next((item for item in items_list if item.tag == tag), None)

        if item is None:
            return -1
        
        total_price += item.calculate_cost(count)
        
    return total_price





