
import turtle
n=int(input("Enter the no. of side: "))
turtle.Screen().bgcolor("black")
sc=turtle.Screen()
sc.setup(400,400)
turtle.title("Polygon Maker")
board=turtle.Turtle()
for i in range(n):
    board.pencolor("white")
    board.backward(100)
    board.left(360/n)
    i+=1
turtle.done()