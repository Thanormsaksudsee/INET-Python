print('Please select operation  -')
print('Add \nSubreact \nMultiply \nDivede')

Select = int(input('Select operation form 1,2,3,4 : '))

if  Select == 0 or Select >= 5:
    print("operation error")

else :

    Num1 = int(input('Enter first number : '))
    Num2 = int(input('Enter second number : '))
    if Select == 1:
        result = Num1 + Num2
        print(" %d + %d = %d " %(Num1,Num2,result))
    elif Select == 2:
        result = Num1 - Num2
        print(" %d - %d = %d " %(Num1,Num2,result))
    elif Select == 3:
        result = Num1 * Num2
        print(" %d * %d = %d " %(Num1,Num2,result))
    elif Select == 4:
        result = Num1 / Num2
        print(" %d / %d = %d " %(Num1,Num2,result))





