

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_map = {"A" : 50, "B" : 30, "C" : 20, "D" : 15}
    a_count = 0
    b_count = 0
    total_price = 0

    for item in skus:
        total_price += price_map[item]

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



