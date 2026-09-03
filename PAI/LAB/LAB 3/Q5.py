import random as rd
stock_prices = [rd.randint(1,1000)for i in range(100)]
day_profits ={}
for i  in range(1000):
    if i == 0:
        day_profits[i] = stock_prices
    else:
        day_profits[i] = [day_profits[i-1][j] +rd.randint(1,100) for j in range(100)]
def max_profit():
    print(day_profits[0])
    while True:
        ans = int(input("Which stock do you want?"))
        if ans in stock_prices:
            break
    ans_ind =0
    for index,stock in enumerate(stock_prices):
        if ans == stock:
            ans_ind = index
    while True:
        sell = int(input("When do you want to sell"))
        if sell in day_profits and sell != 0:
            break

    print("maximum profit you can expect is " , day_profits[sell][ans_ind] - ans)

max_profit()

