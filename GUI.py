import time
import tkinter as tk
from tkinter import ttk
from a_star import astar
from bfs import breath_first_search
from dfs import depth_first_graph_search
import index
import maze
from tkinter import messagebox

sizeOfMatrix = 20
sizeOfCell = 25


class Game(tk.Frame):
    def __init__(self, window):
        self.window = window
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('Project AI')
        self.main_grid = tk.Frame(
            self, bg="black", bd=3, width=400, height=400)
        self.main_grid.grid(pady=(15, 10), padx=(15, 380))

    def make_GUI(self):
        # Matrix-------------------------------------------------------------------------
        self.cells = []
        for i in range(sizeOfMatrix):
            for j in range(sizeOfMatrix):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg="white",
                    width=sizeOfCell,
                    height=sizeOfCell)
                cell_frame.grid(row=i, column=j, padx=1, pady=1)

        # Title----------------------------------------------------------------------------
        title_frame = tk.Frame(self)
        title_frame.place(x=730, y=26, anchor="center")
        tk.Label(title_frame, text="Project AI", font=(
            "Times", 24, "bold"), fg="red").grid(row=0)

        # Label Choose algorithm-----------------------------------------------------------
        labelChooseAlgorithm = tk.Frame(self)
        labelChooseAlgorithm.place(x=648, y=92, anchor="center")
        tk.Label(labelChooseAlgorithm, text="Choose Algorithm:",
                 font=("Times", 14, "bold"), fg="black").grid(row=0)

        # ComboBox-------------------------------------------------------------------------
        self.selectAlgorithm = tk.StringVar()
        comboboxAlgorithm_frame = tk.Frame(self)
        comboboxAlgorithm_frame.place(x=730, y=80)
        comboboxAlgorithm = ttk.Combobox(
            comboboxAlgorithm_frame, width=30, textvariable=self.selectAlgorithm)
        # Adding combobox drop down list
        comboboxAlgorithm['values'] = (
            "BFS - Breadth First Search", "A* - A Star", "DFS - Depth First Search")
        comboboxAlgorithm.grid(column=1, row=5)
        comboboxAlgorithm.current()

        # Button run------------------------------------------------------------------------
        btnRun = tk.Button(self, text="Run Program", font=("Times", 12, "bold"), bg="black",
                           fg="white", width=15, bd=0, command=lambda: self.setColorWithSolution())
        btnRun.place(x=791, y=340)

        # Button Clear------------------------------------------------------------------------
        btnClear = tk.Button(self, text="Clear Program", font=(
            "Times", 12, "bold"), bg="black", fg="white", width=15, bd=0, command=lambda: self.clearScreen())
        btnClear.place(x=575, y=340)

        # Label title note----------------------------------------------------------
        labelNote = tk.Frame(self)
        labelNote.place(x=606, y=400, anchor="center")
        tk.Label(labelNote, text="NOTE: ", font=(
            "Times", 14, "bold underline"), fg="black").grid(row=0)

        # Label Note Red-------------------------------------------------------------------------------
        lableRed_frame = tk.Frame(self)
        lableRed_frame.place(x=590, y=440, anchor="center")
        tk.Label(lableRed_frame, bg='red', width=4, height=2).grid(row=0)

        # Label Note Red text-------------------------------------------------------------------------------
        labelRedText_frame = tk.Frame(self)
        labelRedText_frame.place(x=698, y=440, anchor="center")
        tk.Label(labelRedText_frame, text=": Đích (Quán Cà phê)",
                 font=("Times", 14, "roman"), fg="black").grid(row=0)

        # Label Note Yellow-------------------------------------------------------------------------------
        lableYellow_frame = tk.Frame(self)
        lableYellow_frame.place(x=590, y=490, anchor="center")
        tk.Label(lableYellow_frame, bg='yellow', width=4, height=2).grid(row=0)

        # Label Note Yellow text-------------------------------------------------------------------------------
        labelYellowText_frame = tk.Frame(self)
        labelYellowText_frame.place(x=668, y=490, anchor="center")
        tk.Label(labelYellowText_frame, text=": Nơi xuất phát",
                 font=("Times", 14, "roman"), fg="black").grid(row=0)

        # Label Note Black-------------------------------------------------------------------------------
        lableBlack_frame = tk.Frame(self)
        lableBlack_frame.place(x=590, y=543, anchor="center")
        tk.Label(lableBlack_frame, bg='black', width=4, height=2).grid(row=0)

        # Label Note Black text-------------------------------------------------------------------------------
        labelBlackText_frame = tk.Frame(self)
        labelBlackText_frame.place(x=726, y=543, anchor="center")
        tk.Label(labelBlackText_frame, text=": Tường (Đường cụt, hẻm cụt)", font=(
            "Times", 14, "roman"), fg="black").grid(row=0)

    def inputValues_GUI(self):
        # Label Title InitX----------------------------------------------------------------
        titleChooseInit_frame = tk.Frame(self)
        titleChooseInit_frame.place(x=622, y=130, anchor="center")
        tk.Label(titleChooseInit_frame, text="Input Initial",
                 font=("Times", 14, "bold"), fg="black").grid(row=0)

        # Init X-------------------------------------------------------------------------------
        # Label Enter InitX----------------------------------------------------------------
        titleInputInitX_frame = tk.Frame(self)
        titleInputInitX_frame.place(x=602, y=160, anchor="center")
        tk.Label(titleInputInitX_frame, text="Enter x:", font=(
            "Times", 14, "roman"), fg="black").grid(row=0)

        # NumericUpdown InitX--------------------------------------------------------------
        self.textInitX = tk.StringVar()
        spinboxInitX_frame = tk.Frame(self)
        spinboxInitX_frame.place(x=635, y=150)
        spinboxInitX = tk.Spinbox(
            spinboxInitX_frame, from_=0, to=19, width=8, wrap=True, textvariable=self.textInitX)
        spinboxInitX.grid()

        # Init Y-------------------------------------------------------------------------------
        # Label Enter InitY----------------------------------------------------------------
        titleInputInitY_frame = tk.Frame(self)
        titleInputInitY_frame.place(x=602, y=200, anchor="center")
        tk.Label(titleInputInitY_frame, text="Enter y:", font=(
            "Times", 14, "roman"), fg="black").grid(row=0)

        # NumericUpdown InitY--------------------------------------------------------------
        self.textInitY = tk.StringVar()
        spinboxInitY_frame = tk.Frame(self)
        spinboxInitY_frame.place(x=635, y=190)
        spinboxInitX = tk.Spinbox(
            spinboxInitY_frame, from_=0, to=19, width=8, wrap=True, textvariable=self.textInitY)
        spinboxInitX.grid()

        # Label Title Goal----------------------------------------------------------------
        titleChooseGoal_frame = tk.Frame(self)
        titleChooseGoal_frame.place(x=850, y=130, anchor="center")
        tk.Label(titleChooseGoal_frame, text="Input Goal", font=(
            "Times", 14, "bold"), fg="black").grid(row=0)

        # Goal X-------------------------------------------------------------------------------
        # Label Enter GoalX----------------------------------------------------------------
        titleInputGoalX_frame = tk.Frame(self)
        titleInputGoalX_frame.place(x=835, y=160, anchor="center")
        tk.Label(titleInputGoalX_frame, text="Enter x:", font=(
            "Times", 14, "roman"), fg="black").grid(row=0)

        # NumericUpdown GoalX--------------------------------------------------------------
        self.textGoalX = tk.StringVar()
        spinboxGoalX_frame = tk.Frame(self)
        spinboxGoalX_frame.place(x=870, y=150)
        spinboxInitX = tk.Spinbox(
            spinboxGoalX_frame, from_=0, to=19, width=8, wrap=True, textvariable=self.textGoalX)
        spinboxInitX.grid()

        # Label Enter GoalY----------------------------------------------------------------
        titleInputGoalY_frame = tk.Frame(self)
        titleInputGoalY_frame.place(x=835, y=200, anchor="center")
        tk.Label(titleInputGoalY_frame, text="Enter y:", font=(
            "Times", 14, "roman"), fg="black").grid(row=0)

        # NumericUpdown GoalY--------------------------------------------------------------
        self.textGoalY = tk.StringVar()
        spinboxGoalY_frame = tk.Frame(self)
        spinboxGoalY_frame.place(x=870, y=190)
        spinboxInitX = tk.Spinbox(
            spinboxGoalY_frame, from_=0, to=19, width=8, wrap=True, textvariable=self.textGoalY)
        spinboxInitX.grid()

        # Label Enter Limit----------------------------------------------------------------
        titleInputLimit_frame = tk.Frame(self)
        titleInputLimit_frame.place(x=630, y=240, anchor="center")
        tk.Label(titleInputLimit_frame, text="Choose Limit:",
                 font=("Times", 14, "bold"), fg="black").grid(row=0)

        # NumericUpdown Limit--------------------------------------------------------------
        self.textLimit = tk.StringVar()
        spinboxLimit_frame = tk.Frame(self)
        spinboxLimit_frame.place(x=690, y=230)
        spinboxInitX = tk.Spinbox(
            spinboxLimit_frame, from_=1, to=400, width=38, wrap=True, textvariable=self.textLimit)
        spinboxInitX.grid()

        # ComboBox Maze-------------------------------------------------------------------------
        self.selectMaze = tk.StringVar()
        comboboxMaze_frame = tk.Frame(self)
        comboboxMaze_frame.place(x=700, y=292)
        comboboxMaze = ttk.Combobox(
            comboboxMaze_frame, width=35, textvariable=self.selectMaze)
        # Adding combobox drop down list
        comboboxMaze['values'] = ("maze", "maze2", "maze3", "maze4", "maze5")
        comboboxMaze.grid(column=1, row=5)
        comboboxMaze.current()

        # Label Choose Maze-----------------------------------------------------------
        labelChooseAlgorithm = tk.Frame(self)
        labelChooseAlgorithm.place(x=630, y=302, anchor="center")
        tk.Label(labelChooseAlgorithm, text="Choose Maze:",
                 font=("Times", 14, "bold"), fg="black").grid(row=0)

    # initial color initialization
    def initColor(self, matrix):
        self.change_Color(self.handleSpinbox(self.textInitX),
                          self.handleSpinbox(self.textInitY), "yellow")
        self.change_Color(self.handleSpinbox(self.textGoalX),
                          self.handleSpinbox(self.textGoalY), "red")
        for i in range(sizeOfMatrix):
            for j in range(sizeOfMatrix):
                if matrix[i][j] == 1:
                    self.change_Color(i, j, "black")

    # Change color for a cell
    def change_Color(self, i, j, color):
        cell_frame = tk.Frame(
            self.main_grid,
            bg=color,
            width=sizeOfCell,
            height=sizeOfCell)
        cell_frame.grid(row=i, column=j, padx=1, pady=1)

    # Change color according to solutions
    def setColorWithSolution(self):
        solution, explored = FindSolution()
        if solution != None and explored != None:
            for i in list(range(1, len(explored))):
                if explored[i] in solution:
                    self.change_Color(
                        explored[i][0], explored[i][1], "#00EE00")
                else:
                    self.change_Color(
                        explored[i][0], explored[i][1], "#6699FF")
                # self.initColor(self.handleSelectMaze())
                time.sleep(0.2)
                self.update()
        else:
            messagebox.showinfo("Thông báo", "Không thể tìm được đường đi")

    # Handle Combobox
    def handleCombobox(self):
        if self.selectAlgorithm.get() == "BFS - Breadth First Search":
            return 1
        elif self.selectAlgorithm.get() == "A* - A Star":
            return 2
        elif self.selectAlgorithm.get() == "DFS - Depth First Search":
            return 3
        else:
            return 4

    # handle select value form Spinbox
    def handleSpinbox(self, element):
        number = element.get()
        if number.isnumeric():
            return int(number)
        else:
            if element is self.textLimit:
                return 140
            else:
                return 19

    # select Maze from combobox
    def handleSelectMaze(self):
        if self.selectMaze.get() == "maze":
            return maze.maze
        elif self.selectMaze.get() == "maze2":
            return maze.maze2
        elif self.selectMaze.get() == "maze3":
            return maze.maze3
        elif self.selectMaze.get() == "maze4":
            return maze.maze4
        elif self.selectMaze.get() == "maze5":
            return maze.maze5
        else:
            return None

    # Handle clear screen
    def clearScreen(self):
        self.make_GUI()
        self.inputValues_GUI()

# ======================================================================================================


solution = []


def FindSolution():
    # Hanle find maze
    matrix = game.handleSelectMaze()

    # Handle find Init and Goal Point
    init = (game.handleSpinbox(game.textInitX),
            game.handleSpinbox(game.textInitY))
    goal = (game.handleSpinbox(game.textGoalX),
            game.handleSpinbox(game.textGoalY))

    # Handle no algorithm selected
    if game.handleCombobox() == 4:
        messagebox.showinfo("Thông báo", "Bạn chưa chọn thuật toán")
    # Handle no maze selected
    if game.handleSelectMaze() == None:
        messagebox.showinfo("Thông báo", "Bạn chưa chọn Maze")

    # Handle find solution
    if matrix[init[0]][init[1]] == 1 or matrix[goal[0]][goal[1]] == 1:
        messagebox.showinfo("Thông báo", "Init hoặc goal trùng với tường")
    else:
        if init == goal:
            messagebox.showinfo("Thông báo", "Init trùng với Goal")
            game.initColor(matrix)
            game.update()
            game.change_Color(init[0], init[1], "#00EE00")
            return [1]
        else:
            # BFS
            if game.handleCombobox() == 1:
                game.initColor(matrix)
                game.update()

                problem = index.MazeProblem(init, goal, matrix)
                solution, explored = breath_first_search(problem)
                print(solution)
                return solution, explored
            # A*
            elif game.handleCombobox() == 2:
                game.initColor(matrix)
                game.update()

                problem = index.MazeProblem(init, goal, matrix)
                solution, explored = astar(matrix, init, goal)
                print(solution)
                return solution, explored

            elif game.handleCombobox() == 3:
                game.initColor(matrix)
                game.update()

                problem = index.MazeProblem(init, goal, matrix)
                solution, explored = depth_first_graph_search(problem)
                return solution, explored


if __name__ == "__main__":
    window = tk.Tk()
    window.resizable(0, 0)
    Tk_Width = 900
    Tk_Height = 650
    positionRight = int(window.winfo_screenwidth()/2 - Tk_Width/2)
    positionDown = int(window.winfo_screenheight()/2 - Tk_Height/2)
    window.geometry("{}x{}+{}+{}".format(950, 580,
                    positionRight, positionDown))
    game = Game(window)

    game.make_GUI()
    game.inputValues_GUI()
    game.mainloop()
