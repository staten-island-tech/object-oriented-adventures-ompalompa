import turtle

class board:
    def back_button():
        turtle.clearscreen()  
        board.mainscreen()

    def screen1setup():
        screen = turtle.Screen()
        screen.setup(width=1.0, height=1.0)
        screen.colormode(255)
        screen.bgcolor(105,105,105)
        screen.bgpic("b1.gif")

    def creditscreen():
        screen = turtle.Screen()
        screen.title("Monopoly Credits")
        board.screen1setup()

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
                board.back_button()

        screen.onscreenclick(on_screen_click)

        screen.mainloop()

    def rulescreen():
        screen = turtle.Screen()
        screen.title("Monopoly Game Rules")
        board.screen1setup()

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
                board.back_button()
                
        screen.onscreenclick(on_screen_click)
        screen.mainloop()


    def gameselection():
        screen = turtle.Screen()
        screen.title("Game Selection")
        board.screen1setup()

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
            gt = None

        def on_screen_click(x, y):
            global gt
            if -200 <= x <= 220: 
                if 40 <= y <= 100: 
                    turtle.clearscreen()
                    board.characterselection()
                    gt = board.gamescreen4()
                elif -40 <= y <= 30:  
                    turtle.clearscreen()
                    board.characterselection()
                    gt = board.gamescreen5()
                elif 260 <= x <= 340 and -315 <= y <= -285:  
                    board.back_button()
        
        screen.onscreenclick(on_screen_click)

        draw_button("Singleplayer", -100, 100)
        draw_button("Multiplayer", -100, 0)
        draw_button("Back", 300, -300)
        screen.mainloop()




    def characterselection():
        screen = turtle.Screen()
        screen.title("Character Selection")
        board.screen1setup()
        ct = None

        title = turtle.Turtle()
        title.hideturtle()
        title.penup()
        title.goto(0, 300)
        title.color("white")
        title.write("Select a Character", align="center", font=("Futura", 64, "bold"))

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

        characterlist2 = [
            "Cat",
            "Penguin",
            "Rubber Ducky",
            "Thimble"
        ]

        characters.goto(-900, 220)
        characters.penup()

        for character in characterlist1:
            characters.forward(300)
            characters.right(90)
            characters.forward(0)
            characters.right(-90)
            characters.penup()
            characters.write(character, font=("Arial", 24, "normal"))

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

        def on_screen_click(x, y):
            global ct
            if -950 <= y <= 900: 
                if -950 <= x <= 100: 
                    turtle.clearscreen()
                    board.gt()
                    ct = 'battleship'
                elif -40 <= x <= 30:  
                    turtle.clearscreen()
                    board.gt()
                    ct = 'race car'
                elif -140 <= x <= -100: 
                    turtle.clearscreen()
                    board.gt()
                    ct = 'top hat'
                elif -225 <= x <= -200:  
                    turtle.clearscreen()
                    board.gt()
                    ct = 'scottish terrier'
                elif -950 <= y <= 900:
                    if -40 <= x <= 30:  
                        turtle.clearscreen()
                        board.gt()
                        ct = 'cat'
                    elif -140 <= x <= -100: 
                        turtle.clearscreen()
                        board.gt()
                        ct = 'penguin'
                    elif -225 <= x <= -200:  
                        turtle.clearscreen()
                        board.gt()
                        ct = 'rubber ducky'
                    elif 260 <= x <= 340:
                        turtle.clearscreen()
                        board.gt()
                        ct = 'thimble'
                    elif 260 <= x <= 340 and -315 <= y <= -285:  
                        board.back_button()

        screen.onscreenclick(on_screen_click)

        turtle.mainloop()


    def namepick():
        print("hi3")

    def gamescreen4():
        print("hi4")


    def gamescreen5():
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
        board.screen1setup()

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
                    board.gameselection()
                elif -40 <= y <= 30:  
                    turtle.clearscreen()
                    board.rulescreen() 
                elif -140 <= y <= -100: 
                    turtle.clearscreen()
                    board.creditscreen() 
                elif -225 <= y <= -200:  
                    turtle.bye()

        screen.onscreenclick(on_screen_click)

        draw_button("Play", -100, 100)
        draw_button("Rules", -100, 0)
        draw_button("Credits", -100, -100)
        draw_button("Quit", -100, -200)

        turtle.mainloop()
board.mainscreen()
