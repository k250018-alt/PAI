a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
operator = input('Enter operator: ')
if operator == '+':
    print(a-(-b))
if operator == '-':
    print(a-b)
if operator == '*':
    print(a*b)
if operator == '/':
    print(a/b)