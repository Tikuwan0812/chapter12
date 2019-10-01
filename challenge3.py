class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return self.base * self.height / 2

a_triangle = Triangle(12, 6)
print(a_triangle.calculate_area())