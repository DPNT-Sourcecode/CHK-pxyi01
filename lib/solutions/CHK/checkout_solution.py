price_map = {"A" : 50, "B" : 30, "C" : 20, "D" : 15}
discount_amount = {"A": 20, "B": 15}
discount_item_count = {"A" : 3, "B" : 2}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_counts = {"A": 0, "B": 0}
    total_price = 0
    a_count = 0
    b_count = 0

    for item in skus:
        total_price += price_map[item]
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



