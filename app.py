import subprocess

try:
    answer = int(input("Text Based Game or Tkinter Based (BOTH UNFINISHED BC WE'RE GREAT AT MANAGING TIME!) (1=Text Based, 2=Tkinter): "))
    if answer == 1:
        subprocess.Popen(["python", "data/textbased/textbased.py"])
    elif answer == 2:
        subprocess.Popen(["python", "data/tkinterboard.py"])
    else:
        print("Invalid choice enter 1 or 2.")
except ValueError:
    print("Please enter a valid integer (1 or 2)")
