# coding=utf-8
import turtle as t


direction_map = {'a':180, 's': 270, 'd': 0, 'w': 90, 'q': 135, 'e': 45}
while True:

    UserInput = input("please enter a, s, d, w, q, e and distance with '-': ")
    Input = UserInput.split('-')
    if len(Input) == 2:
        turtleDirection = Input[0]
        turtleDistance = Input[1]
        if direction_map.__contains__(turtleDirection) :
            t.setheading(direction_map[turtleDirection])
            t.forward(int(turtleDistance))
    else:
        break
t.circle(100)
t.done()

