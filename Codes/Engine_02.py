# ENGINE_02
# Carlos Terreros Sanchez

# Import modules
import tkinter as tk

FONT = ('Verdana', 12)

class Engine(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side='top', fill='both', expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        
        frame.grid(row=0, column=0, sticky='nsew')
        
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

def qp(quickprint):
    print(quickprint)

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Start page', font=FONT)
        label.pack(padx=10, pady=10)
        
        button = tk.Button(self, text='Go to page 1',
                           command=lambda: qp('This is passing vars through'))
        button.pack()

program = Engine()
program.mainloop()
