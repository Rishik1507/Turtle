import turtle
turtle.Screen().bgcolor("orange")
sc=turtle.Screen()
sc.setup(400,400)
turtle.title("Hello World!!")
board=turtle.Turtle()
for i in range(4):
    board.backward(100)
    board.left(90)
    i+=1
turtle.done()