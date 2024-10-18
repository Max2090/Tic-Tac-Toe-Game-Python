import tkinter # GUI 

def set_tile(row, column):
    pass

def new_game():
    pass

playerX = "X"
playerO = "O"
current_palyer = playerX

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "blue"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

#window 
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_palyer+"'s turns", font = ("Consolas", 20), background=color_gray,
                      foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range (3):
        board[row][column] = tkinter.Button(frame, text= "", font=("Consolas", 50, "bold"), 
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()


window.mainloop() #keep window active
