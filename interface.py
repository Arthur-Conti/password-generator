import os
import platform

so = platform.system()
if so == "Windows":
    command = "cls"
else:
    command = "clear"

def welcome():
    os.system(command)
    print("Welcome to your personal key generator")
    input("Press ENTER to start")
    
    