'''
Created on Sep 17, 2017

@author: YOUR NAME HERE
'''

def classAverage(data):
    NumberofGrades = 33
    Totalpoints = 0
    while NumberofGrades > 0:
        NumberofGrades -= 1
        list = data[NumberofGrades]
        Totalpoints = Totalpoints + float(list[1])
    return(Totalpoints/33)

def maxGrade(data):
    my_list = data
    Q = 0
    x = 0
    while x < len(my_list):
        print(my_list[x][1])
        if my_list[x][1] > my_list[Q][1]:
            Q = x

        x += 1
    return my_list[Q][1]

def process(name):
    f = open(name)
    answer = []
    for line in f:
        line = line.strip()
        answer.append(line)
    return answer

if __name__ == '__main__':
    filename = "grades.txt"
    data = process(filename)
    students = []
    for each in data:
        students.append(each.split(";"))
    print ("Average grade is ", classAverage(students))
    print ("Maximum grade is ", maxGrade(students))
    grade1 = 80
    grade2 = 90
    print "Names of people with grades between ", grade1, " and ", grade2, " inclusive"
    #names = namesForGrades(data, grade1, grade2)
    # ADD CODE TO PRINT the names one per line
    year1 = 1995
    year2 = 1997
    print ("Number born from ",year1,"to",year2,"is",)
    #print howManyInRange(data, year1, year2)
