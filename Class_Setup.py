class Jelly:
    '''
    An object in this class represents a single diagram in an expansion of the jellyfish relations.
    The calculations will return a sum of jelly objects.
    '''
    def __init__(self, scalar, n, outputs):
        self.scalar = scalar
        self.circles = []
        self.strings = []
        self.n = n
        self.endpoints = []
        self.outputs = outputs

        if not (type(n) == int and n > 0):
            raise TypeError("'n' must be a positive integer")

        if not (type(n) == int and n >= 0):
            raise TypeError("'n' must be a nonnegative integer")

        for i in range(outputs):
            if i % 2 == 0:
                self.endpoints.append(Endpoint(self, i, "Red"))
            if i % 2 == 1:
                self.endpoints.append(Endpoint(self, i, "Blue"))

    def add_circle(self, circle):
        if len(circle.endpoints) == 4*self.n:
            self.circles.append(circle)
        elif len(circle.endpoints) > 4*self.n:
            raise TypeError('This circle has too many strings')
        elif len(circle.endpoints) < 4*self.n:
            raise TypeError('This circle has too few strings')


    def add_string(self, new_string):
        if type(new_string.start) == Endpoint and new_string.start.used:
            raise TypeError('The starting point of this string is already used')
        if type(new_string.end) == Endpoint and new_string.end.used:
            raise TypeError('The ending point of this string is already used')
        if not new_string.start.color == new_string.color:
            raise TypeError('This string and its endpoints have different colors')
        if type(new_string.start) == Endpoint:
            new_string.start.string = new_string    
            new_string.start.used = True
        if type(new_string.end) == Endpoint:
            new_string.end.string = new_string    
            new_string.end.used = True
        if type(new_string.start) == Vertex:
            if new_string.start.used == 3:
                raise TypeError("The starting Vertex is already full")
            new_string.start.strings.append(new_string)
            new_string.start.used += 1
        if type(new_string.end) == Vertex:
            if new_string.end.used == 3:
                raise TypeError("The ending Vertex is already full")
            new_string.end.strings.append(new_string)
            new_string.end.used += 1
        self.strings.append(new_string)


class Circle:
    '''
    An object in this class represents a single "U" or "U*" circle in a jellyfish diagram.
    '''
    def __init__(self, n, starred):
        self.starred = starred
        self.endpoints = []
        self.n = n

        if not (type(n) == int and n > 0):
            raise TypeError("'n' must be a positive integer")

        if starred == True:
            for i in range(4*n):
                if i % 2 == 0:
                    self.endpoints.append(Endpoint(self, i, 'Blue'))
                else:
                    self.endpoints.append(Endpoint(self, i, 'Red'))
        elif starred == False:
            for i in range(4*n):
                if i % 2 == 1:
                    self.endpoints.append(Endpoint(self, i, 'Blue'))
                else:
                    self.endpoints.append(Endpoint(self, i, 'Red'))
        else:
            raise TypeError("'Starred' must be a Boolean")




class String:
    '''
    An object in this class represents a single string, with two endpoints and a color.
    '''
    def __init__(self, start, end, color):
        self.start = start
        self.end = end
        self.color = color

        if not type(start) in {Endpoint, Vertex}:
            raise TypeError("'start' must be an Endpoint object or a Vertex object")
        if not type(end) in {Endpoint, Vertex}:
            raise TypeError("'end' must be an Endpoint object or a Vertex object")
        if not (color in {"Red", "Blue"}):
            raise TypeError("a String's color must be either 'Red' or 'Blue'")



        if (type(start) == Vertex or type(end) == Vertex) and (not color == "Red"):
            raise TypeError("Strings connected to vertices must be red")
        if not start.color == end.color:
            raise TypeError('The endpoints of this string have different colors')
        if start == end and (not (type(start) == Vertex)):
            raise TypeError("A string cannot have the same start and end point, unless the endpoint is a vertex")


class Endpoint:
    '''
    An object in this class represents an endpoint, with a target (a circle object or a jelly object),
    a number (which position on the target), a color ("Red" or "Blue"), and a Boolean for if the endpoint has a string yet.
    '''
    def __init__(self, target, position, color):
        self.target = target
        self.position = position
        self.color = color
        self.used = False
        self.string = None
                
        if not (type(target) in {Circle, Jelly}):
            raise TypeError("'target' must be either a circle or a jelly")
        if type(target) == Circle and (not (type(position) == int and position >= 0 and position <= 4*target.n)):
            raise TypeError("An endpoint's position must be on the target")
        if type(target) == Jelly and (not (type(position) == int and position >= 0 and position <= target.outputs)):
            raise TypeError("An endpoint's position must be on the target")
        

class Vertex:
    '''
    A trivalent vertex that takes three strings, always red.
    Vertex.used gives the number of strings currently ending at the vertex.  One of 0, 1, 2, or 3.
    Right now it's not possible to make a pair of vertices that are connected.  I think that's okay, but I don't like it.
    '''
    def __init__(self, endpoint1, endpoint2, endpoint3):
        self.color = "Red"
        self.used = 0
        self.strings = []

        if not (type(endpoint1) in {Endpoint, Vertex} and type(endpoint2) in {Endpoint, Vertex} and type(endpoint3) in {Endpoint, Vertex}):
            raise TypeError("Endpoints must be either Endpoint objects or Vertex objects")
        if not endpoint1.color == "Red":
            raise TypeError("Endpoint 1 must be red")
        if not endpoint2.color == "Red":
            raise TypeError("Endpoint 2 must be red")
        if not endpoint3.color == "Red":
            raise TypeError("Endpoint 3 must be red")
