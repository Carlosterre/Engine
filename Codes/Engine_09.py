# ENGINE_09
# Carlos Terreros Sanchez

# IMPORT MODULES
import sys
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

# VERSIONS
print ('Python version:', sys.version)                                         # Python version: 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
print('Matplotlib version:', matplotlib.__version__)                           # Matplotlib version: 3.4.2
print('Tkinter version:', tk.TkVersion)                                        # Tkinter version: 8.6

LARGE_FONT= ('Verdana', 12)
MEDIUM_FONT= ('Verdana', 10)
SMALL_FONT= ('Verdana', 8)

class Engine(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.iconbitmap(self, default='Pistons.ico')
        tk.Tk.wm_title(self, 'Engine')
        
        # CONTAINER
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # MENU BAR
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Save',
                             command = lambda: popupmsg('Not supported yet'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.destroy)
        menubar.add_cascade(label='Menu', menu=filemenu)
        
        tk.Tk.config(self, menu=menubar)
        
        # FRAMES
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
    
    def __init__(self, parent, controller, *args, **kwargs):
        
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        label = tk.Label(self, text='Welcome', font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        
        # BUTTON
        button = ttk.Button(self, text='Go to data',
                            command=lambda: controller.show_frame(Data))
        button.pack()
        
class Data(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        label_frame = tk.Label(self, text='Data', font=LARGE_FONT)
        label_frame.pack(padx=10, pady=10)
        
        # USER INPUT    
        self.par = {}
        
        label1 = tk.Label(self, text='Entry 1 (mm)', font=MEDIUM_FONT)         # Entry 1 (mm)
        label1.pack()
        
        self.entry1 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry1.insert(tk.END, '46')
        self.entry1.pack(padx=10, pady=10)
        
        label2 = tk.Label(self, text='Entry 2', font=MEDIUM_FONT)              # Entry 2
        label2.pack()
        
        self.entry2 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry2.insert(tk.END, '74')
        self.entry2.pack(padx=10, pady=10)
        
        # BUTTONS
        button1 = ttk.Button(self, text='Run',
                             command=lambda: self.run())
        button1.pack()
        
        button2 = ttk.Button(self, text='Go to graphs',
                            command=lambda: controller.show_frame(Graphs))
        button2.pack()
    
    def run(self):                                                             # <-
        
        e1_ = float(self.entry1.get())
        e2 = float(self.entry2.get())
        
        # CALCULATIONS
        e1 = e1_ / 1E3                                                         # Entry 1 (m)
        
        for parameter in ['e1', 'e2']:
            self.par[parameter] = eval(parameter)
        
        print(self.par)
        
class Graphs(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        label = tk.Label(self, text='Graphs', font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        
        # TEST FUNCTION                                                        # !
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        # BUTTON
        button = ttk.Button(self, text='Back to data',
                            command=lambda: controller.show_frame(Data))
        button.pack()
        
        # TOOLBAR
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
