import circle
import rectangle


areaCircleChoice = 1
circumferenceChoice = 2
areaRectangleChoice = 3
perimeterRectangleChoice = 4
quitChoice = 5

def main():
    choice = 0
    while choice != quitChoice:
        displayMenu()
        choice = int(input('Endter your choice '))
        if choice == areaCircleChoice:
            radius = float(input("Enter the circle's radius"))
            print('The area is', circle.area(radius))
        elif choice == circumferenceChoice:
            radius = float(input("Enter the circle's radius"))
            print('The circumference is',circumferenceChoice(radius))
        elif choice == areaRectangleChoice:
            width = float(input("Enter te rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The area is', rectangle.area(width, length))
        elif choice == perimeterRectangleChoice:
            width = float(input("Endter the rectangle's width: "))
            lengh = float(input("Enter the rectangle's length"))
            print('The periceter is', rectangle.perimeter(width, lengh))   
        elif choice == quitChoice:
            print('Exuting the program...')
        else:
            print('Error: invalid section.')
def displayMenu():
    print('          MENU')
    print('1) Area of a circle ')
    print('2) Circumference of a circle ')
    print('3) Area of a rectangle ')
    print('4) Perimeter of a rectangle ')
    print('5) Quit ')   
            

main()


