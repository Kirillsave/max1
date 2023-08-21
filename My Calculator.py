list_op=['+','-','/','*']
print(*list_op)
mat_op=input('Выберете одну из этих операций: ')
while True:
    if mat_op not in list_op:
        print(*list_op)
        mat_op=input('Выбранная вами операция не подходит выберете одну из предложенных: ')
    else:
        break
while True:
    try:
        num1=int(input('Введи 1 целое число: '))
        break
    except:
        print('Такой тип данных не допустим')
while True:
    try:
        num2=int(input('Введи 2 целое число: '))
        break
    except:
        print('Такой тип данных не допустим')
if mat_op=='+':
    print(num1+num2)
elif mat_op=='-':
    print(num1-num2)
elif mat_op=='*':
    print(num1*num2)
elif mat_op=='/':
    if num2!=0:
        print(num1/num2)
    else:
        print('На ноль делить нельзя:)')
