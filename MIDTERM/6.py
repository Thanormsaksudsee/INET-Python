keep = "y"

while keep == 'y' :
        word = input('enter word: ')
        word = word.upper()
        index = 0
        sum = []
        while index < len(word) :
                if word[index] == ' ' :
                        sum.append('1')
                elif word[index] == 'A' or word[index] == 'B' or word[index] == 'C':
                        sum.append('2')
                elif word[index] == 'D'or word[index] == 'E' or word[index] == 'F':
                        sum.append('3')
                elif word[index] == 'G'or word[index] == 'H' or word[index] == 'I':
                        sum.append('4')
                elif word[index] == 'J'or word[index] == 'K' or word[index] == 'L':
                        sum.append('5')
                elif word[index] == 'M'or word[index] == 'N' or word[index] == 'O':
                        sum.append('6')
                elif word[index] == 'P'or word[index] == 'Q' or word[index] == 'R':
                        sum.append('7')
                elif word[index] == 'S'or word[index] == 'T' or word[index] == 'U' or word[index] == 'V':
                        sum.append('8')
                elif word[index] == 'W'or word[index] == 'X' or word[index] == 'Y' or word[index] == 'Z':
                        sum.append('9')
                
                index += 1
        print(''.join(sum))
               
                
        keep = input('Endter y: ')
        