import tkinter as Tk
import os

game = 'Q3.py'

def start_game():
    root.destroy()
    os.system(game)    

def show_instructions():
    new_window = Tk.Toplevel(root)
    new_window.title("Instructions")
    new_window.geometry("300x250")
    
    label = Tk.Label(new_window, text="The instructions are very simple:\n\nUse W to go forward\nS to move backward\n And A/D for left/right\nAnd press SPACE for a quick boost\n\nMake sure to get all the ...\nAnd avoid...")
    label.pack(pady=10)

    back_button = Tk.Button(new_window, text="Back to Main Menu", command=new_window.destroy)
    back_button.pack(pady=10)

def quit_menu():
    print("Goodbye! Thanks for playing.")
    root.destroy()


root = Tk.Tk()
root.title("Game Main Menu")
root.configure(bg="darkslategrey")
root.geometry("500x400")

title_label = Tk.Label(root, text=" Main Menu", font=("OCR A EXTENDED", 30), bg="darkslategray", fg="orange")
title_label.pack(pady=50)

def start_game_click():
    start_game()

def show_instructions_click():
    show_instructions()

def quit_game_click():
    quit_menu()


# Create buttons for menu options 
start_button = Tk.Button(root, text="Start Game", font=("OCR A EXTENDED", 15), command=start_game_click, bg="orange", fg="navajowhite", activebackground="moccasin", width=20)
start_button.pack(pady=10)

instructions_button = Tk.Button(root, text="Instructions", font=("OCR A EXTENDED", 15), command=show_instructions_click, bg="orange", fg="navajowhite",activebackground="moccasin", width=20)
instructions_button.pack(pady=10)


quit_button = Tk.Button(root, text="Quit", font=("OCR A EXTENDED", 15), command=quit_game_click, bg="orange", fg="navajowhite", activebackground="moccasin", width=20)
quit_button.pack(pady=10)

root.mainloop()
