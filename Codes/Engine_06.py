# ENGINE_06
# Carlos Terreros Sanchez

# Import modules
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

print('matplotlib version:', matplotlib.__version__)
print('tkinter version:', tk.TkVersion)

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
        
        for F in (StartPage, PageOne, PageTwo, PageThree):
            
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
        label = tk.Label(self, text='Start page', font=FONT)
        label.pack(padx=10, pady=10)
        
        button1 = ttk.Button(self, text='Go to page 1',
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        
        button2 = ttk.Button(self, text='Go to page 2',
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        button3 = ttk.Button(self, text='Go to graph page',
                            command=lambda: controller.show_frame(PageThree))
        
        button3.pack()
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page 1', font=FONT)
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
        label = tk.Label(self, text='Page 2', font=FONT)
        label.pack(padx=10, pady=10)
        
        button1 = ttk.Button(self, text='Go to page 1',
                            command=lambda: controller.show_frame(PageOne))
        
        button1.pack()
        
        button2 = ttk.Button(self, text='Go to start page',
                            command=lambda: controller.show_frame(StartPage))
        
        button2.pack()
        
class PageThree(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Graph page', font=FONT)
        label.pack(padx=10, pady=10)
        
        button = ttk.Button(self, text='Go to start page',
                            command=lambda: controller.show_frame(StartPage))
        
        button.pack()
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
program = Engine()
program.mainloop()
