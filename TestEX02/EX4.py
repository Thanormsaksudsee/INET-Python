
print('Please select operation  -')
print('Add \nSubreact \nMultiply \nDivede')

Select = int(input('Select operation form 1,2,3,4 : '))

if  Select == 1:
    Num1 = int(input('Enter first number : '))
    Num2 = int(input('Enter second number : '))
    print(" %d + %d = %d " % (Num1 ,Num2, Num1 + Num2))
elif Select == 2:
    Num1 = int(input('Enter first number : '))
    Num2 = int(input('Enter second number : '))
    print(" %d + %d = %d " % (Num1 ,Num2, Num1 - Num2))
elif Select == 3:
    Num1 = int(input('Enter first number : '))
    Num2 = int(input('Enter second number : '))
    print(" %d + %d = %d " % (Num1 ,Num2, Num1 * Num2))
elif Select == 4:
    Num1 = int(input('Enter first number : '))
    Num2 = int(input('Enter second number : '))
    print(" %d + %d = %d " % (Num1 ,Num2, Num1 / Num2))

else :
    print