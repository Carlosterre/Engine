# ENGINE_08
# Carlos Terreros Sanchez

# Import modules
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

print('matplotlib version:', matplotlib.__version__)                           # matplotlib version: 3.4.2
print('tkinter version:', tk.TkVersion)                                        # tkinter version: 8.6

LARGE_FONT= ('Verdana', 12)
MEDIUM_FONT= ('Verdana', 10)
SMALL_FONT= ('Verdana', 8)

class Engine(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.iconbitmap(self, default='Pistons.ico')
        tk.Tk.wm_title(self, 'Engine')
        
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Save',
                             command = lambda: popupmsg('Not supported yet'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.destroy)
        menubar.add_cascade(label='Menu', menu=filemenu)

        tk.Tk.config(self, menu=menubar)
        
        self.frames = {}
        
        for F in (Welcome, Data, Graphs):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
            
        self.show_frame(Welcome)
    
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

class Welcome(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Welcome', font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        
        button = ttk.Button(self, text='Go to data',
                            command=lambda: controller.show_frame(Data))
        button.pack()
        
class Data(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text='Data', font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        
        button1 = ttk.Button(self, text='Run')
        button1.pack()
        
        button2 = ttk.Button(self, text='Go to graphs',
                            command=lambda: controller.show_frame(Graphs))
        button2.pack()
        
class Graphs(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Graphs', font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        button = ttk.Button(self, text='Back to data',
                            command=lambda: controller.show_frame(Data))
        button.pack()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def popupmsg(msg):
    
    popup = tk.Tk()
    popup.wm_title('Warning')
    label = ttk.Label(popup, text=msg, font=MEDIUM_FONT)
    label.pack(side='top', fill='x', pady=10)
    
    button = ttk.Button(popup, text='Ok', command = popup.destroy)
    button.pack()
    
    popup.mainloop()

program = Engine()
program.geometry("1280x720")
program.mainloop()
