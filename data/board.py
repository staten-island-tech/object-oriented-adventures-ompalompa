import turtle

def gamescreen():
    screen = turtle.Screen()
    screen.title("Monopoly Game")
    screen.setup(width=810, height=810)
    screen.colormode(255)
    screen.bgcolor(208, 239, 229)


    screen.bgpic("board.gif")

    turtle.done()

def bankscreen():
    print("bankscreen")

def creditscreen():
    print("creditscreen")

def rulescreen():
    screen = turtle.Screen()
    screen.bg(".gif")
    screen.setup(width=800, height=600)

def mainscreen():
    screen = turtle.Screen()
    screen.title("Monopoly Main Screen")
    screen.setup(width=800, height=600)
    screen.colormode(255)
    screen.bgpic("mainscreenbackground.gif")

    button = turtle.Turtle()
    button.hideturtle()
    button.speed(0)

    def draw_button(label, x, y):
        button.penup()
        button.goto(x, y)
        button.fillcolor(199, 0, 0)
        button.begin_fill()
        for _ in range(2):
            button.forward(200)
            button.right(90)
            button.forward(50)
            button.right(90)
        button.end_fill()
        button.penup()
        button.goto(x + 100, y - 37)
        button.color("white")
        button.write(label, align="center", font=("Arial", 16, "bold"))

    def on_screen_click(x, y):
        if -100 <= x <= 100: 
            if -25 <= y <= 25: 
                turtle.clearscreen()
                gamescreen() 
            elif -75 <= y <= -25:  
                turtle.clearscreen()
                rulescreen()  
            elif -125 <= y <= -75: 
                turtle.clearscreen()
                creditscreen() 
            elif -175 <= y <= -125:  
                turtle.bye()

    screen.onscreenclick(on_screen_click)

    draw_button("Play", -100, 0)
    draw_button("Rules", -100, -50)
    draw_button("Credits", -100, -100)
    draw_button("Quit", -100, -150)

    turtle.mainloop()

mainscreen()