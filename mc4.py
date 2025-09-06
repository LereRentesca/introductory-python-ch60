product_cart = [100,200,300,400,500]

def calculate_total(list):
    total = 0
    for value in product_cart:
        total += value
    return total

def calculate_average(total,lenght):
    return total / lenght

total = calculate_total(product_cart)
avg = calculate_average(total, len(product_cart))

print(f"The total is {total} and the average is: {avg}")