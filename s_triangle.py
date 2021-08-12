import sys
import turtle

#turtle.setup(width=1200, height=1200, startx=0, starty=0)


z = turtle.Turtle()
z.pensize(1)
z.speed(0)
#z1=turtle.Screen()
#z1.tracer(0, 0)

x = 20

def t(x):
    z.begin_fill()
    z.setheading(180)

    z.right(120)
    z.forward(x)

    z.right(120)
    z.forward(x)

    z.right(120)
    z.forward(x)

    z.end_fill()



def tr(w):
    if w == 1:
        t(x)
    else:
        tr(w-1)
        z.right(120)
        z.forward(x*2**(w-2))
        tr(w-1)
        z.left(120)
        z.forward(x*2**(w-2))
        tr(w-1)
        z.forward(x*2**(w-2))


def mainP():
    y = int(input("Podaj liczbę powtórzen:"))
    tr(y)

    f = input("Jeszcze raz? T/N")
    turtle.clearscreen()
    if f == 'T':

        mainP()
    else:
        sys.exit()

mainP()
#tr(5)
turtle.mainloop()
