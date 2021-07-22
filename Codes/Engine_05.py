# ENGINE_05
# Carlos Terreros Sanchez

# Import modules
import tkinter as tk
from tkinter import ttk

FONT = ('Verdana', 12)

class Engine(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.iconbitmap(self, default='Pistons.ico')
        tk.Tk.wm_title(self, "Engine")
        
        container = tk.Frame(self)
        
        container.pack(side='top', fill='both', expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):
            
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky='nsew')
            
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Start page', font=FONT)
        label.pack(padx=10, pady=10)
        
        button1 = ttk.Button(self, text='Go to page 1',
                            command=lambda: controller.show_frame(PageOne))

        button1.pack()
        
        button2 = ttk.Button(self, text='Go to page 2',
                            command=lambda: controller.show_frame(PageTwo))
        
        button2.pack()

class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page 1', font=FONT)
        label.pack(padx=10, pady=10)
        
        button1 = ttk.Button(self, text='Go to start page',
                            command=lambda: controller.show_frame(StartPage))

        button1.pack()
        
        button2 = ttk.Button(self, text='Go to page 2',
                            command=lambda: controller.show_frame(PageTwo))
        
        button2.pack()
        
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page 2', font=FONT)
        label.pack(padx=10, pady=10)
        
        button1 = ttk.Button(self, text='Go to page 1',
                            command=lambda: controller.show_frame(PageOne))

        button1.pack()
        
        button2 = ttk.Button(self, text='Start page',
                            command=lambda: controller.show_frame(StartPage))
        
        button2.pack()

program = Engine()
program.mainloop()
