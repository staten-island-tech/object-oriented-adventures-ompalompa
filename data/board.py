import turtle

def creditscreen():
    screen = turtle.Screen()
    screen.title("Monopoly Credits")
    screen.setup(width=1.0, height=1.0)
    screen.colormode(255)
    screen.bgcolor(105,105,105)
    # screen.bg(".gif")

    credits = turtle.Turtle()
    credits.hideturtle()
    credits.penup()
    credits.color("white")
    credits.goto(-350, 250)
    credits.pendown()

    creditlist = [
        "Jonathan Ou",
        "",
        "Alvin Huang",
        "",
        "Aaron Li"
    ]

    credits.write("Monopoly Credits:", align="center", font=("Futura", 48, "bold"))
    credits.penup()
    credits.goto(-350, 220)
    credits.pendown()

    for credit in creditlist:
        credits.penup()
        credits.forward(0)
        credits.right(90)
        credits.forward(30)
        credits.right(-90)
        credits.pendown()
        credits.write(credit, font=("Arial", 24, "normal"))

    screen.mainloop()

def rulescreen():
    screen = turtle.Screen()
    # screen.bg(".gif")
    screen.setup(width=1.0, height=1.0)
    screen.title("Monopoly Game Rules")
    screen.colormode(255)
    screen.bgcolor(105,105,105)

    rules = turtle.Turtle()
    rules.hideturtle()
    rules.penup()
    rules.color("white")
    rules.goto(-350, 250)
    rules.pendown()

    rulelist = [
        "1. Each player starts with $1500.",
        "2. Roll two six-sided dice to move around the board.",
        "3. Buy properties, build houses and hotels, collect rent.",
        "4. If you land on or pass 'GO', collect $200.",
        "5. Land on other players' properties to pay them rent; the amount depends on the development of the property.",
        "6. Draw cards when you land on Chance and Community Chest.",
        "7. Avoid going to Jail. You cannot collect rent in Jail unless you have a Get Out of Jail Free card or pay $50.",
        "8. Bankruptcy ends the game for you; the last player standing wins.",
        "9. Houses and hotels can be sold back to the bank for half the purchase price.",
        "10. Properties can be mortgaged to the bank for loan money.",
        "11. Use strategic trades to acquire monopolies and build developments.",
        "12. The game continues until all but one player has gone bankrupt.",
        "13. Players may form agreements during trades, including selling properties and renting deals.",
        "14. The Utilities and Railroads have special rules for rent calculation based on dice rolls.",
        "15. No player can borrow money from another player."
    ]

    rules.write("Monopoly Rules:", align="center", font=("Futura", 38, "bold"))
    rules.penup()
    rules.goto(-350, 220)
    rules.pendown()

    for rule in rulelist:
        rules.penup()
        rules.forward(0)
        rules.right(90)
        rules.forward(30)
        rules.right(-90)
        rules.pendown()
        rules.write(rule, font=("Arial", 14, "normal"))

    screen.mainloop()



def gamescreen1():
    print("hi")

def gamescreen2():
    print("hi")

def gamescreen3():
    print("hi")

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

def mainscreen():
    screen = turtle.Screen()
    screen.title("Monopoly Main Screen")
    screen.setup(width=1.0, height=1.0)
    screen.colormode(255)
    screen.bgcolor(105,105,105)
    # screen.bgpic("bg1.gif")

    button = turtle.Turtle()
    button.hideturtle()
    button.speed(0)

    title = turtle.Turtle()
    title.hideturtle()
    title.penup()
    title.goto(0, 150)
    title.color("white")
    title.write("Monopoly", align="center", font=("Futura", 64, "bold"))


    def draw_button(label, x, y):
        button.penup()
        button.goto(x, y)
        button.fillcolor(105,105,105)
        button.begin_fill()
        for _ in range(2):
            button.forward(200)
            button.right(90)
            button.forward(50)
            button.right(90)
        button.end_fill()
        button.penup()
        button.goto(x + 100, y - 35)
        button.color("white")
        button.write(label, align="center", font=("Futura", 26, "bold"))

    def on_screen_click(x, y):
        if -100 <= x <= 100: 
            if -25 <= y <= 75: 
                turtle.clearscreen()
                gamescreen() 
            elif -75 <= y <= -25:  
                turtle.clearscreen()
                rulescreen() 
            elif -175 <= y <= -125: 
                turtle.clearscreen()
                creditscreen() 
            elif -275 <= y <= -225:  
                turtle.bye()

    screen.onscreenclick(on_screen_click)

    draw_button("Play", -100, 100)
    draw_button("Rules", -100, 0)
    draw_button("Credits", -100, -100)
    draw_button("Quit", -100, -200)

    turtle.mainloop()
mainscreen()