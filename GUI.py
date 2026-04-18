import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import grid
import Backtrack
import AC3
import time
class SudokuApp:
    x=900
    y=600
    filename="bg.jpg"
    def set_background(self,filename):
        orignal_image=Image.open(filename)
        resized_image=orignal_image.resize((self.x,self.y),Image.Resampling.LANCZOS)
        self.bg_photo=ImageTk.PhotoImage(resized_image)
        self.bg_label=tk.Label(self.root,image=self.bg_photo)
        self.bg_label.place(x=0,y=0,relwidth=1,relheight=1)
        
    def __init__(self,root):#Constructor
        self.root=root
        self.root.title("Sudoku CSP Solver")
        geometry=f"{self.x}x{self.y}"
        self.root.geometry(geometry)
        self.set_background(self.filename)
        self.main_menu()
    
    def clear_screen(self):
        for i in self.root.winfo_children():
            i.destroy()
    def main_menu(self):
        self.clear_screen()
        self.set_background(self.filename)
        normal_color = "#229954"
        hover_color = "#025725"
        title = tk.Label(
            self.root, 
            text="Sudoku Master", 
            font=("Helvetica", 24, "bold"),
            bg="#d8cec9",
            padx=1,
            pady=1
        )
        title.pack(pady=(40,0))
        
        btn_full=tk.Button(
            self.root,
            text="Full Solve Mode",
            command=self.start_full_solve,
            width=13,height=1,font=("Helvetica",20),
            bg=normal_color,
            fg="white",
            activebackground=hover_color,
            activeforeground="white",
            bd=10
        )
        btn_full.pack(pady=(200,0))
        
        btn_User=tk.Button(
            self.root,
            text="User Solve Mode",
            command=self.start_user_solve,
            width=14,height=1,font=("Helvetica",20),
            bg=normal_color,
            fg="white",
            activebackground=hover_color,
            activeforeground="white",
            bd=10
        )
        btn_User.pack(pady=(20,0))
        btn_Exit=tk.Button(
            self.root,
            text="Exit",
            command=self.root.quit,
            width=8,height=1,font=("Helvetica",20),
            bg=normal_color,
            fg="white",
            activebackground=hover_color,
            activeforeground="white",
            bd=10
        )
        btn_Exit.pack(pady=(20,0))
        
        
    def start_full_solve(self):    
        self.clear_screen()
        self.current_game=GameScene(self.root,self,mode="Full")
    
    
    
    def start_user_solve(self):
        self.clear_screen()
        self.current_game=GameScene(self.root,self,mode="User")
    


class GameScene:
    def validate(self):
        self.vcmd=(self.root.register(self.validate_and_check),'%P','%W')
    def validate_and_check(self,P,W):
        if P=="":
            return True
        if len(P)==1 and P.isdigit() and P!="0":
            self.root.after_idle(lambda:self.check_user_logic(P,W))
            return True
        return False
    def check_user_logic(self,value,W):
        if getattr(self,'is_hinting',False):# it will find that if is_hinting have value false
            return
        cell=self.root.nametowidget(W)
        coords=next(k for k,v in self.cells.items() if str(v)==W)
        r,c=coords
        cell.config(fg="Orange")
        
        
        if hasattr(self,'solution') and self.solution:
            correct_val=self.solution[(r,c)]
            if int(value)==int(correct_val):
                cell.config(fg="green",disabledforeground="green",state="disabled")
            else:
                cell.config(fg="red")
    
    
    
    def __init__(self,root,app_instance,mode):
        self.root=root
        self.app=app_instance
        self.mode=mode
        self.is_hinting=False
        self.algo_var=tk.StringVar(value="Backtracking")
        self.level_Var=tk.StringVar(value="Easy")
        self.puzzle_num_var=tk.StringVar(value="1")
        
        self.validate()
        
        # 1. Main Container(900x600)
        self.container=tk.Frame(self.root,bg="white")
        self.container.place(x=0,y=0,width=900,height=600)
        # 2. Sudoku Area (Left 600x600)
        self.Sudoku_frame=tk.Frame(
            self.container,
            bg="white",
            width=600,
            height=600,
            bd=2,
            relief="sunken"
            
        )
        self.Sudoku_frame.pack(side="left")
        self.Sudoku_frame.pack_propagate(False)
        title=tk.Label(
            self.Sudoku_frame,
            text="Sudoku Master", 
            font=("Helvetica", 24, "bold"),
            bg="#d8cec9",
            padx=1,
            pady=1
        )
        title.pack(pady=(40,0))
        # 3. Controls Area (Right 300x600)
        self.controls_area = tk.Frame(self.container, bg="#f4f4f4", width=300, height=600, bd=2, relief="sunken")
        self.controls_area.pack(side="right", fill="y")
        self.controls_area.pack_propagate(False)
        self.cells={}
        self.draw_grid()
        self.draw_controls()


    def draw_grid(self):
        grid_container=tk.Frame(
            self.Sudoku_frame,
            bg="black",
            bd=2
        )
        grid_container.place(relx=0.5,rely=0.5,anchor="center")
        for box_row in range(3):
            for box_col in range(3):
                box_frame=tk.Frame(
                    grid_container,
                    bg="white",
                    highlightbackground="black",
                    highlightthickness="2",
                    bd=0
                )
                box_frame.grid(row=box_row, column=box_col)
                for r in range(3):
                    for c in range(3):
                        global_r=box_row*3+r
                        global_c=box_col*3+c
                        cell=tk.Entry(
                            box_frame,
                            width=2,
                            font=("Helvetica", 24, "bold"),
                            justify="center",
                            bd=1,
                            validate="key",
                            validatecommand=self.vcmd,
                            relief="solid"
                        )
                        cell.grid(row=r,column=c,padx=1,pady=1)
                        cell.bind("<FocusIn>", lambda e: e.widget.config(bg="#6ff1bd"))
                        cell.bind("<FocusOut>", lambda e: e.widget.config(bg="white"))
                        self.cells[(global_r,global_c)]=cell





    def draw_controls(self):
        tk.Label(self.controls_area,text="Select Level",
                 font=("Arial",12,"bold")
                 ).pack(pady=(20,5))
        levels=["easy","medium","high"]
        self.level_var = tk.StringVar(value="Easy")
        tk.OptionMenu(self.controls_area,self.level_var,*levels).pack(pady=10)
        
        tk.Label(self.controls_area,text="Puzzle Number",
                 font=("Arial",12,"bold")
                 ).pack(pady=(20,5))
        self.puzzle_num_var = tk.StringVar(value="1")

        for i in range(1, 5):
            tk.Radiobutton(
                self.controls_area,
                text=f"Puzzle Number {i}",
                variable=self.puzzle_num_var,
                value=str(i),
                font=("Arial", 12)
            ).pack(anchor="w", padx=20)
    
        tk.Label(self.controls_area, text="Algorithm", font=("Arial", 12, "bold")).pack(pady=(20, 5))
        tk.Radiobutton(self.controls_area, text="Backtracking", variable=self.algo_var, value="Backtracking").pack(anchor="w", padx=20)
        tk.Radiobutton(self.controls_area, text="AC-3", variable=self.algo_var, value="AC-3").pack(anchor="w", padx=20)    
        
        self.complexity_label = tk.Label(self.controls_area, text="Complexity: O(9^(n²))", fg="blue")
        self.complexity_label.pack(pady=10)
        tk.Button(self.controls_area, text="LOAD PUZZLE", command=self.load_selected_puzzle, bg="#2ecc71", fg="white", width=20).pack(pady=10)
        if self.mode=="Full":
            
            tk.Button(self.controls_area, text="SOLVE", command=self.solve_puzzle, bg="#3498db", fg="white", width=20).pack(pady=10)
        else:
            tk.Button(self.controls_area, text="Get Hint", command=self.get_hint, bg="#3498db", fg="white", width=20).pack(pady=10)
        tk.Button(self.controls_area, text="RESET", command=self.reset_grid, bg="#e74c3c", fg="white", width=20).pack(pady=10)
        tk.Button(self.controls_area, text="BACK", command=self.app.main_menu, width=20).pack(pady=(30, 0))

    def get_hint(self):
        #1 which cell is focused
        widget=self.root.focus_get()
        #2 is it cell of sudoku board
        if widget in self.cells.values():
            #3 validate if already filled or disabled
            if widget.cget("state")=="disabled":
                messagebox.showinfo("Hint", "This cell is already part of the puzzle!")
                return
            #4 we got cell now find its coordinates
            coords=next(k for k,v in self.cells.items() if v==widget)
            r,c=coords
            
            if hasattr(self,'solution'):
                self.is_hinting=True
                val=self.solution[(r,c)]
                
                widget.config(state="normal")
                widget.delete(0,tk.END)
                widget.insert(0,str(val))
                widget.config(state="normal")
                self.root.after(10,lambda: widget.config(fg="#31C6EB",disabledforeground="#31C6EB",state="disabled"))
                self.is_hinting=False
        else:
            messagebox.showwarning("Hint", "Please click an empty cell first!")
    def load_selected_puzzle(self):
        sudoku_grid = grid.read_sudoku(self.level_var.get(), self.puzzle_num_var.get())
        if sudoku_grid is None:
            messagebox.showerror("Error", "Puzzle file not found")
            return
        self.reset_grid()
        self.root.update_idletasks()
        for r in range(9):
            for c in range(9):
                value = sudoku_grid[r][c]
                cell = self.cells[(r, c)]
                if value != 0:
                    cell.config(state="normal")
                    cell.delete(0, tk.END)     
                    cell.insert(0, str(value))
                    cell.config(
                        fg="black",
                        disabledforeground="black",
                        state="disabled"
                    )
        self.domains,self.assignment,self.constraints=grid.Setup_CSP(sudoku_grid)
        if self.mode=="User":
            self.solve_puzzle()        
        print(f"Loading {self.level_var.get()}_puzzle{self.puzzle_num_var.get()}")

    def solve_puzzle(self):
        self.complexity_label.config(text="solving...",fg="orange")
        self.root.update()
        
        start_time=time.perf_counter()
        
        
        if self.algo_var.get()=="Backtracking":
            self.solution=Backtrack.simple_backtrack(self.assignment,self.domains,self.constraints)
        else:
            self.solution=AC3.solve_with_ac3(self.assignment,self.domains,self.constraints)    
         
        end_time=time.perf_counter()
        execution_time=end_time-start_time 
           
        if self.solution is not None:
            time_text = f"Time: {execution_time:.4f} seconds"
            self.complexity_label.config(text=time_text, fg="darkgreen")
            if self.mode=="Full":
                self.display_solution(self.solution)
        else:
            self.complexity_label.config(text="Failed",fg="red")
            messagebox.showerror(
            "Unsolvable Puzzle", 
            "The algorithm could not find a valid solution for this puzzle.\n\n"
            "Please check if the initial numbers follow Sudoku rules!"
            )
    def reset_grid(self):
        self.solution = None
        self.complexity_label.config(text="Complexity: O(9^(n²))", fg="blue")
        
        for cell in self.cells.values():
            cell.config(state="normal")
            cell.delete(0, tk.END)
            cell.config(
                bg="white",
                fg="black",
                disabledforeground="black"
            )
        
        self.root.update_idletasks()
                
            
    def display_solution(self,solution):
        for r in range(9):
            for c in range(9):
                cell=self.cells[(r,c)]
                if cell.get()=="" or cell.get()=="0":
                    cell.delete(0,tk.END)
                    cell.insert(0,str(solution[(r,c)]))
                    cell.config(fg="green",disabledforeground="green",state="disabled")
                    self.root.update()
                    time.sleep(0.05)
                else:
                    cell.config(fg="black",disabledforeground="black",state="disabled")    

