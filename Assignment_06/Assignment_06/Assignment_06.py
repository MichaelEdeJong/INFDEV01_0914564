from math import sqrt

options = ["square", "hollowsquare", "triangle", "circle", "isosceles"];
option = "";
size = 0;

while True:
    if option in options:
        break
    else:
        option = raw_input("Shape (square, hollowsquare, triangle, circle, isosceles) :")

while True:
    if size:
        break
    else:
        size = raw_input("Size:")

render = ""

if option == "square":
    for y in range(1, int(size)):
        for x in range(1, int(size)):
            render += '*'
        render += '\r\n'

if option == "hollowsquare":
    for y in range(1, int(size)):
        if y == 1 or y == int(size) -1:
            for x in range(1, int(size)):
                render += '*'
        else:
            for x in range(1, int(size)):
                if x == 1 or x == int(size) -1:
                    render += '*'
                else:
                    render += ' '
        render += '\r\n'

elif option == "triangle":
    for y in range(1, int(size)):
        if y < int(size):
            for x in range(1, int(size)):
                if x > y:
                    render += '*'
        render += '\r\n'

elif option == "circle":
    for y in range(1, int(size)):
        diff_y = y -  int(size) / 2
        for x in range(1, int(size)):
            diff_x = x -  int(size) / 2
            dist = sqrt(diff_y * diff_y + diff_x * diff_x);

            if dist <=  int(size) / 2.5:
                render += '*'
            else:
                render += ' '
        render += '\r\n'
elif option == "isosceles":
    for y in range(1, int(size) / 2):
        for x in range(1, int(size)):
            if x > int(size) / 2 - y and x < int(size) / 2 + y:
                render += '*'
            else:
                render += ' '
        render += '\r\n'

print(render)