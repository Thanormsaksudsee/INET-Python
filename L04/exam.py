filename = input('Enter the filename: ')
if filename.endswith('.txt'):
    print('Thast is the name of a text  file.')
elif filename.endswith('.py'):
    print('That is the name of a Python source file.')
elif filename.endswith('.doc'):
    print('That is the name of a word processing dicument.')
else:
    print('Unknown file type.')
    