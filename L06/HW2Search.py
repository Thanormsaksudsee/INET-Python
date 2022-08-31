def main():
    emp_file = open("Display.txt",'r')
    name = input('Enter name your want to find : ')
    for mem in emp_file:
        see = mem.find(name)
        keep = emp_file.readline()
        print(see)
        if see > -1 :
            print('Name:',mem.strip())
            print('ID:',keep.strip())
            keep = emp_file.readline()
            print('dept:',keep.strip())
            keep = emp_file.readline()
            
            


    emp_file.close()
main()