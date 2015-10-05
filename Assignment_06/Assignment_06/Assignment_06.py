options = ["square", "hollowsquare", "triangle"];
option = "";
size = 0;

while True:
    if option in options:
        break
    else:
        option = raw_input("Shape (square, hollowsquare, triangle) :")

while True:
    if size:
        break
    else:
        size = raw_input("Size:")

render = ""

if option == "square":
    for x in range(1, int(size)):
        render += '*' * int(size) + '\r\n'
if option == "hollowsquare":
    for x in range(1, int(size)):
        if x == 1 or x == int(size) -1:
            render += '*' * int(size) + '\r\n'
        else:
            render += '*' + ' ' * (int(size) -2) + '*\r\n'
elif option == "triangle":
    for x in range(1, int(size)):
        if x < int(size):
            render += '*' * x + '\r\n'

print(render)