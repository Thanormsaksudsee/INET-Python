# Homework-02 GPA Calculator
#
# Formular GPA = sum(GradeLevel * Grade Point) / Total Credit
# Grade Point: A = 4, B = 3, C = 2, D = 1, F = 0
# Credit: Math = 3, English = 2, Science = 3, History = 2, Art = 1
# Grade Level: A = 90, B = 80, C = 70, D = 60, F = 0



Credits = {"Computer Programming": 3, "Math": 3, "English": 3, "Physic": 3, "Dance": 1, "Electronic": 3}
Grade_Level = {"A": 80, "B": 70, "C": 60, "D": 50, "F": 0}
Grade_Point = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

Students_Marks = {"John": {"Computer Programming": 80, "Math": 90, "English": 70, "Physic": 50, "Dance": 60, "Electronic": 80}, 
                   "Peter": {"Computer Programming": 85, "Math": 80, "English": 65, "Physic": 60, "Dance": 90, "Electronic": 95}, 
                   "Mary": {"Computer Programming": 45, "Math": 70, "English": 60, "Physic": 65, "Dance": 80, "Electronic": 70},
                   "Tom": {"Computer Programming": 80, "Math": 55, "English": 75, "Physic": 70, "Dance": 75, "Electronic": 80},
                   "Jane": {"Computer Programming": 90, "Math": 95, "English": 80, "Physic": 75, "Dance": 80, "Electronic": 85}}


'''
Expected Output:

Students Grade & GPA
John       Computer Programming : A    Math : A    English : B    Physic : D    Dance : C    Electronic : A    GPA: 3.12
Peter      Computer Programming : A    Math : A    English : C    Physic : C    Dance : A    Electronic : A    GPA: 3.25
Mary       Computer Programming : F    Math : B    English : C    Physic : C    Dance : A    Electronic : B    GPA: 2.12
Tom        Computer Programming : A    Math : D    English : B    Physic : B    Dance : B    Electronic : A    GPA: 3.00
Jane       Computer Programming : A    Math : A    English : A    Physic : B    Dance : A    Electronic : A    GPA: 3.81'''

def main():
    list = []
    for key in Credits:
        list.append(Credits[key])
        cred = sum(list)
    for key in Students_Marks:
        for value in Students_Marks["Peter"]:
            if Students_Marks[key][value] >= 80:
                Students_Marks[key][value] = 'A'
            elif Students_Marks[key][value] >= 70:
                Students_Marks[key][value] = 'B'
            elif Students_Marks[key][value] >= 60:
                Students_Marks[key][value] = 'C'
            elif Students_Marks[key][value] >= 50:
                Students_Marks[key][value] = 'D'
            elif Students_Marks[key][value] <= 50:
                Students_Marks[key][value] = 'F'
    for i,j in Students_Marks.items():
        print(i,'          ',j)



def kido():
    list1 = []
    list2 = []
    for j in Grade_Point:
        print(Grade_Point[j])
        list1.append(Grade_Point[j])
    print(list1)
    for key in Students_Marks:
        for value in Students_Marks["John"]:
            print(Students_Marks[key][value])
            list2.append(Students_Marks[key][value])
    print(list2)
    print(Grade_Point[j]*Students_Marks[key][value])

def bigMom():
    for key in Students_Marks:
        for value in Students_Marks["Peter"]:
            print(Students_Marks[key][value])
    for i,j in Students_Marks.items():
        
        print(i,'          ',j)

