class Polygon(object):
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input("Enter side" + str(i + 1) + ":")) for i in
                      range(self.n)]

    def display_sides(self):
        for i in range(self.n):
            print("Side", (i + 1), "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def find_area(self):
        a, b, c = self.sides
        # find the semi perimeter
        s = (a + b + c)/2
        area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
        print("The area of the triangle is %0.2f" % area)\



# driver code
triangle = Triangle()
triangle.input_sides()
triangle.display_sides()
triangle.find_area()

p = Polygon(4)
p.input_sides()
p.display_sides()
