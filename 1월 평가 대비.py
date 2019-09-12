class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"({self.x}, {self.y})"
    

class Circle:
    def __init__(self,p,r):
        self.center = p
        self.r = r
    
    def get_area(self):
        r = self.r
        return 3.14*r*r
    
    def get_perimeter(self):
        return 2*3.14*self.r

    def get_center(self):
        return self.center.x, self.center.y

    def print(self):
        print(f"Circle: {self.center}, r: {self.r}")

#----------------------
p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()