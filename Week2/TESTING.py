#Random printing thing
'''
Created on Sep 17, 2017

@author: David Han
'''


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
    #print "Average grade is ", classAverage(data)
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

#Robots die
class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()"""

#Minmax code

def MINMAX():
    Numbers = []
    active == True
    while active == True:
        i = int(input("Enter number"))
        h = input("To stop enter 'stop. To continue enter 'Continue'")
        Numbers.append(i)
        if h == 'Stop':
            active = False
        elif h == 'Continue':
            active = True
            ha = sorted(Numbers)
            print(ha)
            print("min = " + str(ha[0]))
            print("max = " + str(ha[-1]))

#Max code from ^^^

Numbers = []
active == True
while active == True:
    i = int(input("Enter number"))
    Numbers.append(i)
        ha = sorted(Numbers)
        print(ha)
        print("max = " + str(ha[-1]))"""

#solarize
from PIL import Image

img = Image.open("dukelogo.png")
pixels = [(int(r), int(g), int(b)) for (r,g,b) in img.getdata()]
list = []
for (r, g, b) in pixels:
    f = 0
    u = 0
    q = 0
    if r < 128:
        f = 255 - r
    elif f == r:
        if g < 128:
            u = 255 - g
        elif u == g:
            if b < 255:
                q = 255 - b
            elif q == b:
                new_pixel = (f, u, q)
                new_pixels.append(new_pixels)
img.putdata(pixels)
img.show()

#de-noise
from PIL import Image

img = Image.open("noise.png")
pixels = [(int(r), int(g), int(b), int(a)) for (r,g,b,a) in img.getdata()]
new_pixels = []
for (r,g,b,a) in pixels:
    return(r*10, g*0, b*0)
    new_pixel = (r, g, b, a)
    new_pixels.append(new_pixel)
img.putdata(new_pixel)
img.show()
