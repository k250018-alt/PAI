import random as rd
import string as st
cart = {}
product =[(''.join(rd.choice(st.ascii_letters) for i in range(10))) for x in range(100)]
for x in product:
    cart[x] = rd.randint(1,10)
print(cart)
add_product = input("Enter the product you want to add: ")
quantity = int(input("Enter the quantity you want to add: "))
if add_product in cart:
    cart[add_product] += quantity
else:
    cart[add_product] = quantity
print(cart)
remove_product = input("Enter the product you want to remove: ")
if remove_product in cart:
    del cart[remove_product]
else:
    print("Product not found.")
print(cart)