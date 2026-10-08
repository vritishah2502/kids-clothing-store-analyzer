#customer information
customer={
    "Name":input("Name:"),
    "Age":int(input("Age:")),
    "City":input("City:"),
    "Phone Number":input("Phone Number:")
  }

num_product=int(input("Enter number of product/s:"))
i=0
list_products=[]

#product innformation
while i<num_product:
    product={
    "Product":input("Product:"),
    "Category":input("Category:"),
    "Quantity":int(input("Quantity:")),
    "Price":float(input("Price:"))
}
    i+=1
    list_products.append(product)

# bill 

#store information
print("\tWELCOME TO ABC KIDS CLOTHING STORE")
print("\t\t\tAHMEDABAD")

#customer
print("\nCustomer Information")
print("Name:",customer.get("Name"))
print("Age:",customer.get("Age"))
print("City:",customer.get("City"))
print("Phone Number:",customer.get("Phone Number"))

#product
print("\nProduct Information")
for product in list_products:
    print("\nProduct:",product.get("Product"))
    print("Category:",product.get("Category"))
    print("Quantity:",product.get("Quantity"))
    print("Price:",product.get("Price"))

#subtotal
subtotal=0
for subt in list_products:
    price=subt.get("Price")
    quantity=subt.get("Quantity")
    sub_total=price*quantity
    subtotal=subtotal+sub_total

print("\nSubtotal:",subtotal)

#discount
if(subtotal<2000):
    discount_percentage=0
elif(subtotal>=2000 and subtotal<5000):
    print("Discount:3%")
    discount_percentage=3
elif(subtotal>=5000 and subtotal<10000):
    print("Discount:7%")
    discount_percentage=7
elif(subtotal>=10000 and subtotal<50000):
    print("Discount:12%")
    discount_percentage=12
else:
    print("Discount:20%")
    discount_percentage=20

#discount amount
if(discount_percentage==0):
   discount_amount=0
else:
    discount_amount = subtotal*discount_percentage/100
    print("Discount Amount:",discount_amount)

#final amounnt
final_amount = subtotal - discount_amount
print("Final Amount:",final_amount)

#amount saved
amount_saved=subtotal-final_amount
if(amount_saved==0):
    pass
else:
    print("Amount Saved: ",amount_saved)

print("\n\tTHANK YOU FOR SHOPPING!")