import string_helpers as helpers
luy = float(input("Please enter your luy number: "))
khr = helpers.convertToKHR(luy)
con = helpers.formatNumber(khr)
print(con)

dis = float(input("Please enter Total: "))
total = int(input("Please enter discount:"))
amount = helpers.calculateDiscount(dis,total)
print(amount)

input = int(input("Input number:"))
result = helpers.formatNumber(input)
print(result)