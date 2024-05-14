import turtle

class screens:
    ct = None
    gt = None
    name = None
    @classmethod
    def set_ct(cls, value):  
        cls.ct = value
    @classmethod
    def set_name(cls, value):
        cls.name = value
    @classmethod
    def set_gt(cls, value):
        cls.gt = value
        
    def back_button():
        turtle.clearscreen()  
        screens.mainscreen()

    def screen1setup():
        screen = turtle.Screen()
        screen.setup(width=1.0, height=1.0)
        screen.colormode(255)
        screen.bgcolor(105,105,105)
        screen.bgpic('data/images/b1.png')

    def creditscreen():
        screen = turtle.Screen()
        screen.title("Monopoly Credits")
        screens.screen1setup()

        credits = turtle.Turtle()
        credits.hideturtle()
        credits.penup()
        credits.color("white")
        credits.goto(-350, 250)
        credits.pendown()

        creditlist = [
            "Jonathan Ou",
            "Alvin Huang",
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
            credits.forward(120)
            credits.right(-90)
            credits.pendown()
            credits.write(credit, font=("Arial", 24, "normal"))

        button = turtle.Turtle()
        button.hideturtle()
        button.color("white")
        button.penup()
        button.goto(0, -250) 
        button.write("Back", align="center", font=("Arial", 20, "bold"))

        def on_screen_click(x, y):
            if -40 <= x <= 40 and -265 <= y <= -235:  
                screens.back_button()

        screen.onscreenclick(on_screen_click)

        screen.mainloop()

    def rulescreen():
        screen = turtle.Screen()
        screen.title("Monopoly Game Rules")
        screens.screen1setup()

        rules = turtle.Turtle()
        rules.hideturtle()
        rules.penup()
        rules.color("white")
        rules.goto(-300, 250)
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
            ""
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

        button = turtle.Turtle()
        button.hideturtle()
        button.color("white")
        button.penup()
        button.goto(300, -300) 
        button.write("Back", align="center", font=("Arial", 20, "bold"))

        def on_screen_click(x, y):
            if 260 <= x <= 340 and -315 <= y <= -285:  
                screens.back_button()
                
        screen.onscreenclick(on_screen_click)
        screen.mainloop()

    def gameselection():
        screen = turtle.Screen()
        screen.title("Game Selection")
        screens.screen1setup()

        button = turtle.Turtle()
        button.hideturtle()
        button.speed(0)
        
        title = turtle.Turtle()
        title.hideturtle()
        title.penup()
        title.goto(0, 300)
        title.color("white")
        title.write("Select a Game Type", align="center", font=("Futura", 64, "bold"))

        def draw_button(label, x, y):
            button.penup()
            button.goto(x, y)
            for _ in range(2):
                button.forward(200)
                button.right(90)
                button.forward(50)
                button.right(90)
            button.end_fill()
            button.penup()
            button.goto(x + 100, y - 43)
            button.color("white")
            button.write(label, align="center", font=("Futura", 26, "bold"))

        def on_screen_click(x, y):
            global gt
            if -200 <= x <= 220: 
                if 40 <= y <= 100: 
                    turtle.clearscreen()
                    screens.characterselection()
                    screens.set_gt('singleplayer')
                elif -40 <= y <= 30:  
                    turtle.clearscreen()
                    screens.characterselection()
                    screens.set_gt('multiplayer')
                elif 260 <= x <= 340 and -315 <= y <= -285:  
                    screens.back_button()
        
        screen.onscreenclick(on_screen_click)

        draw_button("Singleplayer", -100, 100)
        draw_button("Multiplayer", -100, 0)
        draw_button("Back", 300, -300)
        screen.mainloop()

    def characterselection():
        global ct
        ct = None
        screen = turtle.Screen()
        screen.title("Character Selection")
        screens.screen1setup()

        title = turtle.Turtle()
        title.hideturtle()
        title.penup()
        title.goto(0, 300)
        title.color("white")
        title.write("Select a Character", align="center", font=("Futura", 64, "bold"))

        def on_screen_click(x, y):
            global ct
            if -620 <= x <= -450 and 200 <= y <= 260: 
                turtle.clearscreen()
                screens.gamescreen4()
                screens.set_ct('battleship')
            elif -320 <= x <= -150 and 200 <= y <= 260:  
                turtle.clearscreen()
                screens.gamescreen4()
                screens.set_ct('race car')
            elif -20 <= x <= 150 and 200 <= y <= 260: 
                turtle.clearscreen()
                screens.gamescreen4()
                screens.set_ct('top hat')
            elif 280 <= x <= 450 and 200 <= y <= 260:  
                turtle.clearscreen()
                screens.gamescreen4()
                screens.set_ct('scottish terrier')
            elif -620 <= x <= -450 and -220 <= y <= -160:  
                turtle.clearscreen()
                screens.gamescreen5()
                screens.set_ct('cat')
            elif -320 <= x <= -150 and -220 <= y <= -160: 
                turtle.clearscreen()
                screens.gamescreen5()
                screens.set_ct('penguin')
            elif -20 <= x <= 150 and -220 <= y <= -160:  
                turtle.clearscreen()
                screens.gamescreen5()
                screens.set_ct('rubber ducky')
            elif 280 <= x <= 450 and -220 <= y <= -160:
                turtle.clearscreen()
                screens.gamescreen5()
                screens.set_ct('thimble')
            elif 260 <= x <= 340 and -315 <= y <= -285:  
                screens.back_button()

        screen.onscreenclick(on_screen_click)
        characters = turtle.Turtle()
        characters.hideturtle()
        characters.penup()
        characters.color("white")

        characterlist1 = [
            "Battleship",
            "Race Car",
            "Top Hat",
            "Scottish Terrier"
        ]

        characters.goto(-900, 270)
        characters.penup()

        for character in characterlist1:
            characters.forward(300)
            characters.right(90)
            characters.forward(0)
            characters.right(-90)
            characters.penup()
            characters.write(character, font=("Arial", 24, "normal"))
        characterlist2 = [
            "Cat",
            "Penguin",
            "Rubber Ducky",
            "Thimble" 
        ]

        characters.goto(-900, -250)

        for character in characterlist2:
            characters.forward(300)
            characters.right(90)
            characters.forward(0)
            characters.right(-90)
            characters.penup()
            characters.write(character, font=("Arial", 24, "normal"))

        button = turtle.Turtle()
        button.hideturtle()
        button.color("white")
        button.penup()
        button.goto(300, -300) 
        button.write("Back", align="center", font=("Arial", 20, "bold"))

        turtle.mainloop()

    def namepick():
        screen = turtle.Screen()
        screen.title("Monopoly Name")
        screens.screen1setup()
        

        title = turtle.Turtle()
        title.hideturtle()
        title.penup()
        title.goto(0, 150)
        title.color("white")
        title.write("Enter A Name", align="center", font=("Futura", 64, "bold"))

        name = screen.textinput("NIM", "Enter Username:                                                                                                          ")
        screens.set_name(name)        
        turtle.clearscreen()
        screens.gameselection()
    


    def gamescreen4():
        print("hi4")


    def gamescreen5():
        screen = turtle.Screen()
        screen.title("Monopoly Game")
        screen.setup(width=810, height=810)
        screen.colormode(255)
        screen.bgcolor(208, 239, 229)


        screen.bgpic("data/images/board.gif")

        turtle.done()

    def bankscreen():
        screen = turtle.Screen()
        screen.title("Monopoly Bank Screen")
        screens.screen1setup()

    def mainscreen():
        screen = turtle.Screen()
        screen.title("Monopoly Main Screen")
        screens.screen1setup()

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
            for _ in range(2):
                button.forward(200)
                button.right(90)
                button.forward(50)
                button.right(90)
            button.end_fill()
            button.penup()
            button.goto(x + 100, y - 43)
            button.color("white")
            button.write(label, align="center", font=("Futura", 26, "bold"))

        def on_screen_click(x, y):
            if -200 <= x <= 220: 
                if 40 <= y <= 100: 
                    turtle.clearscreen()
                    screens.namepick()
                elif -40 <= y <= 30:  
                    turtle.clearscreen()
                    screens.rulescreen() 
                elif -140 <= y <= -100: 
                    turtle.clearscreen()
                    screens.creditscreen() 
                elif -225 <= y <= -200:  
                    turtle.bye()

        screen.onscreenclick(on_screen_click)

        draw_button("Play", -100, 100)
        draw_button("Rules", -100, 0)
        draw_button("Credits", -100, -100)
        draw_button("Quit", -100, -200)

        turtle.mainloop()
