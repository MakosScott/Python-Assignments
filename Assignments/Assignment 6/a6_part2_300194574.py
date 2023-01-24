# Family name: Scott Makos 
# Student number: 300194574
# Course: IT1 1120 
# Assignment Number 6
# year 2020
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


###############################


class Rectangle:
    'class that represents a triangle in a plane'

    def __init__(self, bottomleft, topright, color):
        ''' (Point,Point, string) -> None
        Defines the coordinates of the bottom left and top right points
        of the rectangle and the color of the rectangle '''
        self.bottomleft = bottomleft
        self.topright = topright
        self.color = color

    def get_bottom_left(self):
        ''' (None)->Point
        Returns the coordenates of the bottom left point of the rectangle'''
        return self.bottomleft

    def get_top_right(self):
        ''' (None)->Point
        Returns the coordenates of the top right point of the rectangle'''
        return self.topright

    def get_color(self):
        '''(None)->string
        Returns a the color of the rectangle'''
        return self.color

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x coordinates of the bottom right and top left points of the
        rectangle by dx and the ycoordinates of the bottom right and top left points of the
        rectang;e by dy'''
        self.bottomleft.x += dx
        self.bottomleft.y += dy
        self.topright.x += dx
        self.topright.y += dy
    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other are the same rectangle'''
        return self.bottomleft == other.bottomleft and self.topright == other.topright
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation of the Rectangle(bottomleft,bottomright, color)'''
        return 'Rectangle('+str(self.bottomleft)+','+ str(self.topright)+','"'"+str(self.color)+"'"+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Rectangle(bottomleft,bottomright, color).
        In this case we chose the same representation as in __repr__'''
        return f"I am a {self.color} rectangle with a bottom left corner at {self.bottomleft} and a top right corner at {self.topright}."

    def reset_color(self,color):
        '''string -> None
        Changes the color of the rectangle to the new color imputed'''
        self.color = color

    def get_perimeter(self):
        '''None -> int
        Returns the perimeter of the rectangle'''
        perim =((self.topright.x- self.bottomleft.x)*2) + ((self.topright.y- self.bottomleft.y)*2)
        return perim
    def get_area(self):
        '''None -> int
        Returns the area of the rectangle'''
        area = ((self.topright.x- self.bottomleft.x))* ((self.topright.y- self.bottomleft.y))
        return area
    def contains(self, coordx, coordy):
        '''None -> int
        Returns True if the point(defined by the x and y coordinates inputted as parameter)
        is within the calling rectangle'''
        check = True
        if not coordx >= self.bottomleft.x :
            check = False
        if not coordx <= self.topright.x :
            check = False
        if not coordy >= self.bottomleft.y :
            check = False
        if not coordy <= self.topright.y :
            check = False
        return check

###############################

class Canvas:
    'class that represents a point in the plane'
    
    def __init__(self):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''

    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Rectangle('+str(self.bottomleft)+','+ str(self.topright)+','"'"+str(self.color)+"'"+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return f"I am a {self.color} rectangle with a bottom left corner at {self.bottomleft} and a top right corner at {self.topright}."
    def count_same_color(self):
        pass
    def add_one_rectangle(rectangle):
        pass
