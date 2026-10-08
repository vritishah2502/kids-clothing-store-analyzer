
from billingsystem import list_products
def calculate_total_unit():
    total_unit=0
    for units in list_products:
        qty=units.get("Quantity")
        total_unit=total_unit+qty
    return total_unit

print("\n\t\tSTORE ANALYSIS")
print("Total units sold:",calculate_total_unit())

def expensive_product():
    max_price=list_products[0]["Price"]
    prod_name=list_products[0]["Product"]
    for value in list_products:
        cost=value.get("Price")
        name=value.get("Product")
        if(max_price<cost):
            max_price=cost
            prod_name=name
    print("Most expensive product price:",max_price)
    return prod_name

print("Most expensive product:",expensive_product())

def category_count():
    group={
        "Female":0,
        "Male":0,
        "Unisex":0
    }
    for cate in list_products:
        kind=cate.get("Category")
        volume=cate.get("Quantity")
        if(kind=="Female"):
            group["Female"] = group["Female"] + volume
        elif(kind=="Male"):
            group["Male"] = group["Male"] + volume
        elif(kind=="Unisex"):
            group["Unisex"] = group["Unisex"]+ volume
    print("Female:", group["Female"])
    print("Male:", group["Male"])
    print("Unisex:", group["Unisex"])

category_count()