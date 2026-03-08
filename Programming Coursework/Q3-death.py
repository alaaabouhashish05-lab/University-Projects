import tkinter as tk
import os

def toggle_visibility():
    if game_over_label.winfo_ismapped():
        game_over_label.grid_remove() 
    else:
        game_over_label.grid()

    root.after(500, toggle_visibility)  
menu = 'Q3-menu.py'
game = 'Q3.py'
def restart():
    root.destroy()
    os.system(game)
    
def main_menu():
    root.destroy()
    os.system(menu)
    
def quit_game():
        print("Goodbye! Thanks for playing.")
        root.destroy()

# The main window
root = tk.Tk()
root.title("Game Main Menu")
root.configure(bg="Red")  # Set the background color
root.geometry("500x400")  # Set the window size

# Create a frame for the "Game Over" label
frame = tk.Frame(root, bg="Red")
frame.pack(expand=True)

# Create a label with some text inside the frame
game_over_label = tk.Label(frame, text="Game over", font=("System", 30), bg="Red", fg="gold")
game_over_label.grid(pady=60)  # Use grid initially instead of pack

# Start the flashing for the "Game Over" label
toggle_visibility()

# Functions to handle button clicks
def start_game_click():
    restart()

def main_menu_click():
    main_menu()

def quit_game_click():
    quit_game()


# Create buttons for menu options outside the frame
start_button = tk.Button(root, text="Restart Level", font=("system", 15), command=start_game_click, width=20)
start_button.pack(pady=10)

menu_button = tk.Button(root, text="Back to main menu", font=("system", 15), command=main_menu_click, width=20)
menu_button.pack(pady=10)


quit_button = tk.Button(root, text="Quit", font=("system", 15), command=quit_game_click, width=20)
quit_button.pack(pady=10)

root.mainloop()
