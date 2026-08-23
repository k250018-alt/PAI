lst = list(map(int,input("Enter numbers separated by spaces").split()))
a = int(input("Enter a number: "))
lst = list(i for i in lst if i>a)
print(lst)