class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self,newWidth):
        self.width = newWidth

    def set_height(self, newHeight):
        self.height = newHeight

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            foto = ""
            for a in range(self.height):
                for b in range(self.width):
                    foto = foto+"*"
                foto = foto + "\n"
            return foto

    def get_amount_inside(self, obj):

        # Checks if size of obj exceeds the size of .self

        total = 0
        if obj.width > self.width or obj.height > self.height:
            return total

        # Uses a loop count to check how many times the obj fits in .self

        b = obj.height
        y = obj.width

        auxHei = b
        auxWid = y

        while auxHei < self.height:
            while auxWid < self.width:
                total = total + 1
                auxWid = auxWid + y
            auxHei = auxHei + b
        return total

    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"


class Square(Rectangle):

    def __init__(self,length):
        self.width=length
        self.height=length

    def set_side(self,length):
        self.width=length
        self.height=length

    def set_width(self,newWidth):
        self.width=newWidth
        self.height=newWidth

    def set_length(self, newHeight):
        self.width=newHeight
        self.height=newHeight

    def __str__(self):
        return "Square(side="+str(self.width)+")"


rect = Rectangle(10, 4)
print(rect.get_area())
rect.set_height(5)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

print (rect.get_amount_inside(sq))