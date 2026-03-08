import tkinter as tk
import os
import random 

game = 'Q3.py'
menu = "Q3-menu.py"

def start_game():
    root.destroy()
    os.system(game)    

def main_menu():
    root.destroy()
    os.system(menu)

def quit_menu():
    print("Goodbye! Thanks for playing.")
    root.destroy()


root = tk.Tk()
root.title("Game Main Menu")
root.configure(bg="darkmagenta")
root.geometry("500x400")

title_label = tk.Label(root, text=" WOOHOOO!!", font=("OCR A EXTENDED", 30), bg="darkmagenta", fg="black")
title_label.pack(pady=20)

def create_flashing_dots(canvas):
    colors = ['red', 'green', 'blue', 'yellow', 'white']
    for _ in range(50):
        x = random.randint(0, 500)
        y = random.randint(0, 400)
        size = random.randint(5, 15)
        color = random.choice(colors)
        canvas.create_oval(x, y, x + size, y + size, fill=color)

def flash_background(canvas, count=0):
    if count % 2 == 0:
        canvas.delete("all")  # Clear canvas on even counts
        create_flashing_dots(canvas)
    root.after(500, flash_background, canvas, count + 1)

def start_game_click():
    start_game()

def main_menu_click():
    main_menu()
    
def quit_game_click():
    quit_menu()

canvas = tk.Canvas(root, width=400, height=130, bg="darkmagenta")
canvas.pack()

flash_background(canvas)  # Start the flashing dots animation

start_button = tk.Button(root, text="Replay", font=("OCR A EXTENDED", 15), command=start_game_click, width=20)
start_button.pack(pady=10)

menu_button = tk.Button(root, text="Back to main menu", font=("OCR A EXTENDED", 15), command=main_menu_click, width=20)
menu_button.pack(pady=10)


quit_button = tk.Button(root, text="Quit", font=("OCR A EXTENDED", 15), command=quit_game_click, width=20)
quit_button.pack(pady=10)

root.mainloop()
