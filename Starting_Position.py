from Class_Setup import *

def Starting_Position_Left(n):


    initial_position = Jelly(1, n, 8*n)

    initial_position.add_circle(Circle(n, False))
    initial_position.add_circle(Circle(n, False))

    for i in range(2*n):
        #Left hand strings into top circle
        if i % 2 == 0:
            initial_position.add_string(String(initial_position.endpoints[i], initial_position.circles[1].endpoints[i], "Red"))
        elif i % 2 == 1:
            initial_position.add_string(String(initial_position.endpoints[i], initial_position.circles[1].endpoints[i], "Blue"))

        #Left hand strings into bottom circle
        if i % 2 == 0:
            initial_position.add_string(String(initial_position.endpoints[2*n+i], initial_position.circles[0].endpoints[i], "Red"))
        elif i % 2 == 1:
            initial_position.add_string(String(initial_position.endpoints[2*n+i], initial_position.circles[0].endpoints[i], "Blue"))

        #Right hand strings into bottom circle
        if i % 2 == 0:
            initial_position.add_string(String(initial_position.endpoints[4*n+i], initial_position.circles[0].endpoints[2*n+i], "Red"))
        elif i % 2 == 1:
            initial_position.add_string(String(initial_position.endpoints[4*n+i], initial_position.circles[0].endpoints[2*n+i], "Blue"))

        #Right hand strings into top circle
        if i % 2 == 0:
            initial_position.add_string(String(initial_position.endpoints[6*n+i], initial_position.circles[1].endpoints[2*n+i], "Red"))
        elif i % 2 == 1:
            initial_position.add_string(String(initial_position.endpoints[6*n+i], initial_position.circles[1].endpoints[2*n+i], "Blue"))

    return initial_position


def Starting_Position_Right(n):


    initial_position = Jelly(1, n, 8*n)

    initial_position.add_circle(Circle(n, False))
    initial_position.add_circle(Circle(n, False))

    for i in range(2*n):
        #Left hand strings into top circle
        if i % 2 == 0:
            initial_position.add_string(String(initial_position.endpoints[i], initial_position.circles[0].endpoints[i], "Red"))
        elif i % 2 == 1:
            initial_position.add_string(String(initial_position.endpoints[i], initial_position.circles[0].endpoints[i], "Blue"))

        #Left hand strings into bottom circle
        if i % 2 == 0:
            initial_position.add_string(String(initial_position.endpoints[2*n+i], initial_position.circles[1].endpoints[i], "Red"))
        elif i % 2 == 1:
            initial_position.add_string(String(initial_position.endpoints[2*n+i], initial_position.circles[1].endpoints[i], "Blue"))

        #Right hand strings into bottom circle
        if i % 2 == 0:
            initial_position.add_string(String(initial_position.endpoints[4*n+i], initial_position.circles[1].endpoints[2*n+i], "Red"))
        elif i % 2 == 1:
            initial_position.add_string(String(initial_position.endpoints[4*n+i], initial_position.circles[1].endpoints[2*n+i], "Blue"))

        #Right hand strings into top circle
        if i % 2 == 0:
            initial_position.add_string(String(initial_position.endpoints[6*n+i], initial_position.circles[0].endpoints[2*n+i], "Red"))
        elif i % 2 == 1:
            initial_position.add_string(String(initial_position.endpoints[6*n+i], initial_position.circles[0].endpoints[2*n+i], "Blue"))

    return initial_position




























    









































