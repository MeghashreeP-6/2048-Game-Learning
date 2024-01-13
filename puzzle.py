import random
#Frame:
    #Python Tkinter Frame widget is used to organize the group of widgets. 
    #It acts like a container which can be used to hold the other widgets. 
#Label:
    #This widget implements a display box where you can place text or images.
#Center:
    #The default for a ttk label is to be aligned left, but the tkinter label is aligned center, 
    #and the order of your imports means that you're using a ttk Label. 
    #The quick fix for your example is to explicitly set the anchor option for the ttk label 
    #(eg: label. configure(anchor="center") ).
from tkinter import Frame, Label, CENTER
import logic
import constants as c 

# def gen():
#     return random.randint(0,c.GRID_LEN -1)

#Initialise a frame
class GridGame(Frame):
    def __init__(self):
        Frame.__init__(self)

        #Grid method is used to create grid
        self.grid()
        self.master.title('2048')
        #bind() method of Tkinter is utilized to connect an event passed in the widget along with the event handler.
        self.master.bind("<Key>", self.key_down)

        self.commands = {
            c.KEY_UP: logic.move_up,
            c.KEY_DOWN: logic.move_down,
            c.KEY_LEFT: logic.move_left,
            c.KEY_RIGHT: logic.move_right,
            c.KEY_UP_ALT1: logic.move_up,
            c.KEY_DOWN_ALT1: logic.move_down,
            c.KEY_LEFT_ALT1: logic.move_left,
            c.KEY_RIGHT_ALT1: logic.move_right,
            c.KEY_UP_ALT2: logic.move_up,
            c.KEY_DOWN_ALT2: logic.move_down,
            c.KEY_LEFT_ALT2: logic.move_left,
            c.KEY_RIGHT_ALT2: logic.move_right
            
        }

        self.grid_cells = []
        self.init_grid()
        self.matrix = logic.start_game(c.GRID_LEN)
        self.history_matrixs = []
        self.update_grid_cells()
        #mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application,
        #wait for an event to occur and process the event as long as the window is not closed.
        self.mainloop()

    #Initialize grid with all the settings. i.e cell and grid colour are filled
    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(
                    background,
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    width=c.SIZE / c.GRID_LEN,
                    height=c.SIZE / c.GRID_LEN
                )
                cell.grid(
                    row=i,
                    column=j,
                    padx=c.GRID_PADDING,
                    pady=c.GRID_PADDING
                )
                t = Label(
                    master=cell,
                    text="",
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=c.FONT,
                    width=5,
                    height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    #Update grid: Change cell colour according to the number present in the grid.
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number]
        
                    )
        #Calls all pending idle tasks, without processing any other events
        self.update_idletasks()

    def key_down(self, event):
        #keysyms - keysyms recognized by Tk.A single-character string that is the key's code (only for keyboard events) keysym.
        # A string that is the key's symbolic name (only for keyboard events)
        key = event.keysym
        print(event)
        if key == c.KEY_QUIT: exit()
        if key == c.KEY_BACK and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.update_grid_cells()
            print('total step:', len(self.history_matrixs))
        elif key in self.commands:
            self.matrix, done = self.commands[key](self.matrix)
            if done:
                self.matrix = logic.add_two(self.matrix)
                # record last move
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
                if logic.game_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.game_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    # def generate_next(self):
    #     index = (gen(), gen())
    #     while self.matrix[index[0]][index[1]] != 0:
    #         index = (gen(), gen())
    #     self.matrix[index[0]][index[1]] = 2

game_grid = GridGame()