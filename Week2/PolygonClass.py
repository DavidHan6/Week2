class Polygon:

    def __init__(self):
        self.list_of_points = []

    def addPoint(self, x, y):
        self.list_of_points.append([x, y])
        return self.list_of_points
        pointx.append(self.list_of_points)

    def dist(self, x1, x2, y1, y2):
        return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

    def perimeter(self):
        self.perimeter = 0.0
        for i in range(len(self.list_of_points)):
            x1 = self.list_of_points[i][0]
            x2 = self.list_of_points[i+1][0]
            y1 = self.list_of_points[i][1]
            y2 = self.list_of_points[i+1][1]
            self.perimeter = self.perimeter + dist(x1, x2, y1, y2)
        return self.perimeter

    def Area(self):
        count = 0
        secondpart = 0
        for i in range(len(self.list_of_points)):
            if count >= len(self.list_of_points)-1:
                first = self.list_of_points [0]
                second = self.list_of_points [len(self.list_of_points)-1]
            else:
                first = self.list_of_points [count]
                second = self.list_of_points [count + 1]
                firstpart = first [0] * second [1] - first [1] * second [0]
            secondpart = secondpart + firstpart
            count += 1
        return abs(secondpart / 2)

changelaterpls = Polygon()
pointx = float(input("WhatpointX1"))
pointy = float(input("WhatpointY1"))
pointx2 = float(input("WhatpointX2"))
pointy2 = float(input("WhatpointY2"))
pointx3 = float(input("WhatpointX3"))
pointy3 = float(input("WhatpointY3"))
pointx4 = float(input("WhatpointY4"))
pointy4 = float(input("WhatpointY4"))
changelaterpls.addPoint(pointx, pointy)
changelaterpls.addPoint(pointx2, pointy2)
changelaterpls.addPoint(pointx3, pointy3)
changelaterpls.addPoint(pointx4, pointy4)
print(changelaterpls.Area())
