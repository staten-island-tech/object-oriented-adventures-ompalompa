import json
from data.board import board
from data.Player import Playeroptions
import turtle

def a():
    def ea():
        nonlocal x  # Use nonlocal to modify the variable in the outer function's scope
        x = 'hi'

    ea()  # Call the inner function to set the value of x

def b():
    a()  # Call function a to set the value of x
    print(x)  # Access the value of x in function b

x = None  # Define x in the global scope

b()  # Call function b
