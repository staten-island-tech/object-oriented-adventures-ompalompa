import subprocess
import time, sys
import os, platform 

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

while True:
    try:
        answer = int(input("Text Based Game or Tkinter Based (BOTH UNFINISHED BC WE'RE GREAT AT MANAGING TIME!) (1=Text Based, 2=Tkinter): "))
        if answer == 1:
            subprocess.Popen(["python", "data/textbased/textbased.py"])

        elif answer == 2:
            subprocess.Popen(["python", "data/tkinterboard.py"])
        else:
            for _ in range(3):  
                for state in ['loading.  ', 'loading.. ', 'loading...']:
                    sys.stdout.write('\r' + state)
                    sys.stdout.flush()
                    time.sleep(0.5)
            print("\ngame loaded")
            time.sleep(1)
            print("ok game over the end")
            time.sleep(1)
            print("kidding you're dumb for picking a invalid number (1 or 2)")
    except ValueError:
        print("Please enter a valid integer (1 or 2)")
