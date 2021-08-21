# ENGINE_11
# Carlos Terreros Sanchez

# IMPORT MODULES
import sys

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation

import tkinter as tk
from tkinter import ttk

import json

# VERSIONS
print ('Python version:', sys.version)                                         # Python version: 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
print('Matplotlib version:', matplotlib.__version__)                           # Matplotlib version: 3.4.2
print('Tkinter version:', tk.TkVersion)                                        # Tkinter version: 8.6

# FONTS
LARGE_FONT= ('Verdana', 12)
MEDIUM_FONT= ('Verdana', 10)
SMALL_FONT= ('Verdana', 8)

# GRAPHS
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(1, 1, 1)

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
                             command = lambda: popupmsg('Not supported yet'))  # Popup
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
        
    def show_frame(self, cont, *args, **kwargs):
        
        frame = self.frames[cont]
        frame.tkraise()
        
class Welcome(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        #LABEL
        label_frame = tk.Label(self, text='Welcome', font=LARGE_FONT)
        label_frame.pack(padx=10, pady=10)
        
        # BUTTON
        button = ttk.Button(self, text='Go to data',
                            command=lambda: controller.show_frame(Data))
        button.pack()
        
class Data(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        # LABEL
        label_frame = tk.Label(self, text='Data', font=LARGE_FONT)
        label_frame.pack(padx=10, pady=10)
        
        # USER INPUT
        self.par = {}
        
        label1 = tk.Label(self, text='Dessign parameters', font=LARGE_FONT)    # Dessign parameters
        label1.pack()
        
        label2 = tk.Label(self, text='Number of cylinders', font=MEDIUM_FONT)  # Number of cylinders
        label2.pack()
        
        self.entry2 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry2.insert(tk.END, '4')
        self.entry2.pack(padx=10, pady=10)
        
        label3 = tk.Label(self, text='Lenght of the stroke (mm)',
                          font=MEDIUM_FONT)                                    # Stroke (mm)
        label3.pack()
        
        self.entry3 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry3.insert(tk.END, '92')
        self.entry3.pack(padx=10, pady=10)
        
        label4 = tk.Label(self, text='Engine displacement (cc)',
                          font=MEDIUM_FONT)                                    # Displacement (cm^3)
        label4.pack()
        
        self.entry4 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry4.insert(tk.END, '1991')
        self.entry4.pack(padx=10, pady=10)
        
        label5 = tk.Label(self, text='Connecting rod lenght / Crank length',
                          font=MEDIUM_FONT)                                    # Lambda
        label5.pack()
        
        self.entry5 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry5.insert(tk.END, '0.25')
        self.entry5.pack(padx=10, pady=10)
        
        label6 = tk.Label(self, text='Compression ratio', font=MEDIUM_FONT)    # Compression ratio
        label6.pack()
        
        self.entry6 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry6.insert(tk.END, '9')
        self.entry6.pack(padx=10, pady=10)
        
        label7 = tk.Label(self, text='Intake closing delay (ª)',
                          font=MEDIUM_FONT)                                    # ICD (º)
        label7.pack()
        
        self.entry7 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry7.insert(tk.END, '20')
        self.entry7.pack(padx=10, pady=10)
        
        
        label8 = tk.Label(self, text='Exhaust opening advance (ª)',
                          font=MEDIUM_FONT)                                    # EOA (º)
        label8.pack()
        
        self.entry8 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry8.insert(tk.END, '20')
        self.entry8.pack(padx=10, pady=10)
        
        label9 = tk.Label(self, text='Octane rating (MON)',
                          font=MEDIUM_FONT)                                    # Octane number
        label9.pack()
        
        self.entry9 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry9.insert(tk.END, '95')
        self.entry9.pack(padx=10, pady=10)
        
        label10 = tk.Label(self, text='Operation parameters', font=LARGE_FONT)  # Operation parameters
        label10.pack()
        
        label11 = tk.Label(self, text='Revolutions per minute',
                          font=MEDIUM_FONT)                                    # RPM
        label11.pack()
        
        self.entry11 = tk.Entry(self, font=MEDIUM_FONT)
        self.entry11.insert(tk.END, '6750')
        self.entry11.pack(padx=10, pady=10)
        
        # BUTTONS
        button1 = ttk.Button(self, text='Run',
                             command=lambda: self.run())
        button1.pack()
        
        button2 = ttk.Button(self, text='Go to graphs',
                            command=lambda: controller.show_frame(Graphs))
        button2.pack()
        
    def run(self, *args, **kwargs):
        
        ncyl = float(self.entry2.get())
        s_ = float(self.entry3.get())
        d = float(self.entry4.get())
        lmbd = float(self.entry5.get())
        rg = float(self.entry6.get())
        icd = float(self.entry7.get())
        eoa = float(self.entry8.get())
        on = float(self.entry11.get())        
        
        rpm = float(self.entry11.get())
        
        # CALCULATIONS
        s = s_ / 1E3                                                           # Stroke (m)
        vd_ = d / ncyl                                                         # Displaced volume (cm^3)
        vd = vd_ / 1E6                                                         # Displaced volume (m^3)
        
        for parameter in ['ncyl', 's', 'vd', 'lmbd', 'rg', 'icd', 'eoa', 'on',
                          'rpm']:
            self.par[parameter] = eval(parameter)
        
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(self.par, file)
        
class Graphs(tk.Frame):
    
    def __init__(self, parent, controller, *args, **kwargs):
        
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        # LABEL
        label_frame = tk.Label(self, text='Graphs', font=LARGE_FONT)
        label_frame.pack(padx=10, pady=10)
        
        # CANVAS
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
        
def popupmsg(msg, *args, **kwargs):
    
    popup = tk.Tk()
    popup.wm_title('Warning')
    
    # LABEL
    label = ttk.Label(popup, text=msg, font=MEDIUM_FONT)
    label.pack(side='top', fill='x', pady=10)
    
    # BUTTON
    button = ttk.Button(popup, text='Ok', command = popup.destroy)
    button.pack()
    
    popup.mainloop()
    
def animate(inpt, *args, **kwargs):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        
    values = [*data.values()]
    
    title = 'Graph'
    a.set_title(title)
    
program = Engine()
ani = animation.FuncAnimation(f, animate, interval=1000)
program.geometry("1280x720")
program.mainloop()
