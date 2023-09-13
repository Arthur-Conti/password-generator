from random import choice
import interface
import os
import platform

so = platform.system()
if so == "Windows":
    command = "cls"
else:
    command = "clear"

def get_size():
    interface.welcome()
    os.system(command)
    try:
        number_carac = int(input("Password size: "))
        get_type(number_carac)
    except:
        print('Error! Type a number.')
        input("Press ENTER to try again")
        get_size()

def get_type(number_carac): 
    os.system(command)
    try:
        print("Your password must contain: ")
        print("1 - Everything you can imagine")
        print("2 - No special characters")
        print("3 - Only numbers")
        choice_id = int(input("Enter your preferred option: "))
        pass_gen(number_carac, choice_id)
    except:
        print('Error! Type a number.')
        input("Press ENTER to try again")
        get_type(number_carac)
    
def pass_gen(number_carac, choice_id):
    passw = []
    if choice_id == 1:
        strings = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","&","*")
    elif choice_id == 2:
        strings = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0")
    elif choice_id == 3:
        strings = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    else:
        print("Not a option")
        input("Press ENTER to try again")
        get_type(number_carac)

    for gen_passw in range(0, int(number_carac)):
        passw.append(choice(strings))

    for carac in passw:
        print(carac, end='')
    
get_size()