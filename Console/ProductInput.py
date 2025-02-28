from tabulate import tabulate

def input_product():
    products = []
    while True:
        productName = input("Enter Product Name: ")
        qty = int(input("Enter Quantity: "))
        while qty < 1:
            qty = int(input("Enter product qty again (1->): "))

        unitPrice = float(input("Enter Unit Price: "))
        while unitPrice < 0:
            unitPrice = float(input("Enter Unit Price (0->): "))

        subt = qty * unitPrice
        products.append({
            "productName": productName,
            "qty": qty,
            "unitPrice": unitPrice,
            "subTotal": subt
        })

        more = input("Add more? (y/n): ")
        while more.lower() not in ("y", "n"):
            more = input("Add more? (y/n): ")
        if more.lower() == "n":
            break
    return products

def input_discount():
    dis = int(input("Enter Discount (0-100): "))
    while dis < 0 or dis > 100:
        dis = int(input("Enter Discount again (0-100): "))
    return dis

def calculate_totals(products, discount):
    total = sum(item["subTotal"] for item in products)
    discount_price = discount / 100 * total
    grand_total_usd = total - discount_price
    grand_total_riel = grand_total_usd * 4100
    return total, discount_price, grand_total_usd, grand_total_riel

def display_output(products, total, discount_price, grand_total_usd, grand_total_riel):
    table = []
    for idx, item in enumerate(products, start=1):
        table.append([
            idx,
            item['productName'],
            item['qty'],
            f"{item['unitPrice']:.2f}",
            f"{item['subTotal']:.2f}"
        ])
    headers = ["No", "Name", "Qty", "Price", "Total"]
    print(tabulate(table, headers=headers, tablefmt="simple_outline"))
    print(f"\nTotal: {total:.2f} USD")
    print(f"Discount: {discount_price:.2f} USD")
    print(f"Grand Total (USD): {grand_total_usd:.2f} USD")
    print(f"Grand Total (Riel): {grand_total_riel:.2f} ៛")

def main():
    products = input_product()
    discount = input_discount()
    total, discount_price, grand_total_usd, grand_total_riel = calculate_totals(products, discount)
    display_output(products, total, discount_price, grand_total_usd, grand_total_riel)

if __name__ == "__main__":
    main()
