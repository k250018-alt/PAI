import random as rd
import string as st
product_database =[({'product id' : rd.choice(st.ascii_uppercase)+str(rd.randint(1,100)),
                    'name': (''.join(rd.choice(st.ascii_uppercase) for i in range(0,10))),
                    'category': rd.choice(st.ascii_uppercase),'stock':rd.randint(0,10)}) for x in range(0,10)]
def update_stock(stock ,product):
    found = False
    for x in product_database:
        if x['product id'] == product:
            found = True
            x['stock'] = stock
            break
    if not found:
        print("wrong product id")
def find_zero():
    found = False
    lst_of_zero = []
    for x in product_database:
        if x['stock'] == 0:
            found = True
            lst_of_zero.append(x)
    if not found:
        print("all stock are filled")
        return
    else:
        print(lst_of_zero)
print(product_database)
product = input("Enter product id: ")
stock = int(input("Enter stock: "))
update_stock(stock , product)
find_zero()