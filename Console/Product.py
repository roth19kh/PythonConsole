items = []
while True:
    productName = input("Enter product name: ")
    productQty = int(input("Enter product QTY: "))
    while productQty <= 0 :
        productQty = int(input("Enter product QTY: "))
    productPrice = float(input("Enter product price: "))
    while productPrice <= 0 :
        productQty = int(input("Enter product QTY: "))
    totalPrice = productPrice * productQty
    items.append({'productName':productName,
                  'productQty':productQty,
                  'productPrice':productPrice,
                  'totalPrice':totalPrice})

    print("| No  |  ProductName  |  ProductQTY  |  ProductPrice  |  TotalPrice  |")
    no =1
    for product in items:
        print("|",no,"  |" ,f"{product['productName']:<5}" ,f"{product['productQty']:<5}" ,f"{product['productPrice']}")
        no=+1
