def calculate_total_value(shares , price) :
    total_position_value = shares*price
    return total_position_value

print(calculate_total_value(10,150.0))





def calc_price(price) :
    new_price = price + (price*0.18)
    return new_price

print(calc_price(250))