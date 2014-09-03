__author__ = 'JDucommun'
from graphics import *


def drawBar(window, year, height):
    # Draw a bar in window
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)


def createLabeledWindow():
    # Returns a GraphWin
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(window)
    Text(Point(-1, 2500), ' 2.5K').draw(window)
    Text(Point(-1, 5000), ' 5.0K').draw(window)
    Text(Point(-1, 7500), ' 7.5K').draw(window)
    Text(Point(-1,10000), ' 10.0K').draw(window)
    return window


def main():
    #Intro
    print("This program plots growth of 10y investment")

    #Get pri and int
    principal = eval(input("Enter initial principal: "))
    apr = eval(input("Enter the APR"))
    win = createLabeledWindow()

    drawBar(win, 0, principal)
    for year in range(1, 11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("Press <Enter> to quit")
    win.close()

main()