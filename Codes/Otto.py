# Carlos Terreros Sanchez

import json

class Engine():
    
    # DESSIGN PARAMETERS
    ncyl = 4                                                                   # Number of cylinders
    s_ = 92                                                                    # Carrera del cilindro (mm)
    cil = 1991                                                                 # Clindrada (cm^3)
    lmbd = 0.25                                                                # Lambda de la biela: lmbd = lb / rb
    rg = 9                                                                     # Relacion de compresion
    rca = 20                                                                   # Retardo al cierre de admision (º)
    aae = 20                                                                   # Adelanto a la apertura del escape (º)
    NO = 95                                                                    # Numero de octanos
    
program = Engine()