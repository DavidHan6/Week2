'''
Created on Sep 17, 2017

@author: David Han
'''

def classAverage(data):
    NumberofGrades = 33
    Totalpoints = []
    while NumberofGrades >= 0:
        NumberofGrades -= 1
        Totalpoints = Totalpoints + 


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
    for each in data:
        print (each)
    print
    print ("Average grade is ", classAverage(data))
    #print "Maximum grade is ", maxGrade(data)
    grade1 = 80
    grade2 = 90
    #print "Names of people with grades between ", grade1, " and ", grade2, " inclusive"
    #names = namesForGrades(data, grade1, grade2)
    # ADD CODE TO PRINT the names one per line
    print
    year1 = 1995
    year2 = 1997
    print ("Number born from ",year1,"to",year2,"is",)
    #print howManyInRange(data, year1, year2)
