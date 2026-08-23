lst = list(map(int,input('Enter the number separated by spaces: ').split()))
even_num = sum(i%2==0 for i in lst)
print(even_num)