

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
            total_price -= 20 

    return total_price



