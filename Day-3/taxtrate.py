def calculateWithTax(price , tax=0.18) :
    priceWithtax = price + (price*tax)

    return priceWithtax

price = int(input("Enter price to get total price with tax : "))
print("price of",price,"with tax is",calculateWithTax(price))
