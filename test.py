import string_helpers as helpers

print("----Store----")
productName = input(str("Please input product name:"))
qty = input("QTY:")
price = input("Price per unit:")
discount = input("Discount%:")

amount = float(qty) * float(price)
discountPrice = str(helpers.calculateDiscount(int(discount),amount))
amountDiscount = amount - float(discountPrice)


print("Product name:" + productName)
print("Quantity:" + str(qty))
print("Discount:" + discount)
print("Discount price:" + str(helpers.calculateDiscount(int(discount),amount)))
print("Amount after discount$:" + str(amountDiscount))
noF = str(helpers.convertToKHR(amount))
print("Amount after discount Riel:" + str(helpers.formatNumber(noF)))


# luy = float(input("Please enter your luy number: "))
# khr = helpers.convertToKHR(luy)
# con = helpers.formatNumber(khr)
# print(con)
#
# dis = float(input("Please enter Total: "))
# total = int(input("Please enter discount:"))
# amount = helpers.calculateDiscount(dis,total)
# print(amount)
#
# input = int(input("Input number:"))
# result = helpers.formatNumber(input)
# print(result)