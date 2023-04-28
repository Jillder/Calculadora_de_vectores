try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk, Image
import numpy as np


class calculadora(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configuración predeterminada
        self.configure(bg = "black")
        font.nametofont("TkDefaultFont").configure(size = 12)
        self.title("Calculadora de vectores")
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
    
        # Contenedor principal
        contenedor_principal = tk.Frame(self, bg = "Purple")
        contenedor_principal.grid( sticky = "nsew")
        
        # Diccionario de frames
        self.todos_los_frames = dict()
        for F in (Frame_eleccion, Frame_select_dimension_escalamiento, Frame_escalamiento2, Frame_r_e_2, Frame_escalamiento3, Frame_r_e_3, Frame_escalamiento4, Frame_r_e_4, Frame_escalamiento5, Frame_r_e_5, Frame_select_dimension_producto, Frame_producto2, Frame_r_p_2, Frame_producto3, Frame_r_p_3, Frame_producto4, Frame_r_p_4, Frame_producto5, Frame_r_p_5, Frame_select_dimension_norma, Frame_norma2, Frame_r_n_2, Frame_norma3, Frame_r_n_3, Frame_norma4, Frame_r_n_4, Frame_norma5, Frame_r_n_5, Frame_select_dimension_angulo, Frame_angulo2, Frame_r_a_2, Frame_angulo3, Frame_r_a_3, Frame_angulo4, Frame_r_a_4, Frame_angulo5, Frame_r_a_5, Frame_select_dimension_distancia, Frame_distancia2, Frame_r_d_2, Frame_distancia3, Frame_r_d_3, Frame_distancia4, Frame_r_d_4, Frame_distancia5, Frame_r_d_5):
            frame = F(contenedor_principal, self)
            self.todos_los_frames[F] = frame
            frame.grid(row=0, column=0, sticky = "nsew")
        
        self.show_frame(Frame_eleccion)

    # Funcion mostrar el frame de seleccion de dimension
    def show_frame(self, contenedor_llamado, *args, **kwargs):
        if (contenedor_llamado == 1):
            contenedor_llamado = Frame_select_dimension_escalamiento
        elif (contenedor_llamado == 2):
            contenedor_llamado = Frame_select_dimension_producto   
        elif (contenedor_llamado == 3):
            contenedor_llamado = Frame_select_dimension_norma
        elif (contenedor_llamado == 4):
            contenedor_llamado = Frame_select_dimension_angulo
        elif (contenedor_llamado == 5):
            contenedor_llamado = Frame_select_dimension_distancia
        else:
            pass

        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise()
        

    # Funcion seleccionar dimension del vector, escalamiento vectorial
    def select_dimension_escalamiento(self, dimension, *args, **kwargs):
        if (dimension == 1):
            dimension = Frame_escalamiento2
        elif (dimension == 2):
            dimension = Frame_escalamiento3  
        elif (dimension == 3):
            dimension = Frame_escalamiento4
        elif (dimension == 4):
            dimension = Frame_escalamiento5
        else:
            pass

        frame = self.todos_los_frames[dimension]
        frame.tkraise()

    # Funcion seleccionar dimension del vector, producto punto
    def select_dimension_producto(self, dimension, *args, **kwargs):
        if (dimension == 1):
            dimension = Frame_producto2
        elif (dimension == 2):
            dimension = Frame_producto3  
        elif (dimension == 3):
            dimension = Frame_producto4
        elif (dimension == 4):
            dimension = Frame_producto5
        else:
            pass

        frame = self.todos_los_frames[dimension]
        frame.tkraise()

    # Funcion seleccionar dimension del vector, norma
    def select_dimension_norma(self, dimension, *args, **kwargs):
        if (dimension == 1):
            dimension = Frame_norma2
        elif (dimension == 2):
            dimension = Frame_norma3  
        elif (dimension == 3):
            dimension = Frame_norma4
        elif (dimension == 4):
            dimension = Frame_norma5
        else:
            pass

        frame = self.todos_los_frames[dimension]
        frame.tkraise()

    # Funcion seleccionar dimension del vector, angulo
    def select_dimension_angulo(self, dimension, *args, **kwargs):
        if (dimension == 1):
            dimension = Frame_angulo2
        elif (dimension == 2):
            dimension = Frame_angulo3  
        elif (dimension == 3):
            dimension = Frame_angulo4
        elif (dimension == 4):
            dimension = Frame_angulo5
        else:
            pass

        frame = self.todos_los_frames[dimension]
        frame.tkraise()

    # Funcion seleccionar dimension del vector, distancia
    def select_dimension_distancia(self, dimension, *args, **kwargs):
        if (dimension == 1):
            dimension = Frame_distancia2
        elif (dimension == 2):
            dimension = Frame_distancia3  
        elif (dimension == 3):
            dimension = Frame_distancia4
        elif (dimension == 4):
            dimension = Frame_distancia5
        else:
            pass

        frame = self.todos_los_frames[dimension]
        frame.tkraise()

#----------------------------Muestra el resultado del escalamiento de 2 dimensiones---------------------------------
    def resultado_escalamiento2d(self, x1, x2, k ,*args, **kwargs):
        
        x1 = x1
        x2 = x2
        k = k
        
        Vector = []

        Vector.append(x1)
        Vector.append(x2)
        Vectorint = [int(x) for x in Vector]
        k = int(k)

        Vectorint = np.array(Vectorint)
        Vector_r = Vectorint*k
        Vector_r.tolist()
              
        frame = self.todos_los_frames[Frame_r_e_2]
        l_1 = tk.Label(frame, text=Vector_r, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del escalamiento de 3 dimensiones
    def resultado_escalamiento3d(self, x1, x2, x3, k, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        k = k
        
        Vector = []

        Vector.append(x1)
        Vector.append(x2)
        Vector.append(x3)
        Vectorint = [int(x) for x in Vector]
        k = int(k)

        Vectorint = np.array(Vectorint)
        Vector_r = Vectorint*k
        Vector_r.tolist()
              
        frame = self.todos_los_frames[Frame_r_e_3]
        l_1 = tk.Label(frame, text=Vector_r, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del escalamiento de 4 dimensiones
    def resultado_escalamiento4d(self, x1, x2, x3, x4, k, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        k = k
        
        Vector = []

        Vector.append(x1)
        Vector.append(x2)
        Vector.append(x3)
        Vector.append(x4)
        Vectorint = [int(x) for x in Vector]
        k = int(k)

        Vectorint = np.array(Vectorint)
        Vector_r = Vectorint*k
        Vector_r.tolist()
              
        frame = self.todos_los_frames[Frame_r_e_4]
        l_1 = tk.Label(frame, text=Vector_r, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del escalamiento de 5 dimensiones
    def resultado_escalamiento5d(self, x1, x2, x3, x4, x5, k, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        x5 = x5
        k = k
        
        Vector = []

        Vector.append(x1)
        Vector.append(x2)
        Vector.append(x3)
        Vector.append(x4)
        Vector.append(x5)
        Vectorint = [int(x) for x in Vector]
        k = int(k)

        Vectorint = np.array(Vectorint)
        Vector_r = Vectorint*k
        Vector_r.tolist()
              
        frame = self.todos_los_frames[Frame_r_e_5]
        l_1 = tk.Label(frame, text=Vector_r, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del producto de 2 dimensiones
    def resultado_producto2d(self, x1, x2, y1, y2, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        y1 = y1
        y2 = y2
        
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        Producto = VectorAint.dot(VectorBint)
        Producto.tolist()
        
        frame = self.todos_los_frames[Frame_r_p_2]
        l_1 = tk.Label(frame, text=Producto, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del producto de 3 dimensiones
    def resultado_producto3d(self, x1, x2, x3, y1, y2, y3, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        y1 = y1
        y2 = y2
        y3 = y3

        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorA.append(x3)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorB.append(y3)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        Producto = VectorAint.dot(VectorBint)
        Producto.tolist()
              
        frame = self.todos_los_frames[Frame_r_p_3]
        l_1 = tk.Label(frame, text=Producto, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del producto de 4 dimensiones
    def resultado_producto4d(self, x1, x2, x3, x4, y1, y2, y3, y4, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        y1 = y1
        y2 = y2
        y3 = y3
        y4 = y4

        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorA.append(x3)
        VectorA.append(x4)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorB.append(y3)
        VectorB.append(y4)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        Producto = VectorAint.dot(VectorBint)
        Producto.tolist()
              
        frame = self.todos_los_frames[Frame_r_p_4]
        l_1 = tk.Label(frame, text=Producto, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del producto de 5 dimensiones
    def resultado_producto5d(self, x1, x2, x3, x4, x5, y1, y2, y3, y4, y5, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        x5 = x5
        y1 = y1
        y2 = y2
        y3 = y3
        y4 = y4
        y5 = y5
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorA.append(x3)
        VectorA.append(x4)
        VectorA.append(x5)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorB.append(y3)
        VectorB.append(y4)
        VectorB.append(y5)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        Producto = VectorAint.dot(VectorBint)
        Producto.tolist()
              
        frame = self.todos_los_frames[Frame_r_p_5]
        l_1 = tk.Label(frame, text=Producto, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado de la norma de 2 dimensiones
    def resultado_norma2d(self, x1, x2, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        
        Vector = []

        Vector.append(x1)
        Vector.append(x2)
        Vectorint = [int(x) for x in Vector]

        Vectorint = np.array(Vectorint)
        Vector_r = np.linalg.norm(Vectorint)
        Vector_r.tolist()
        
        frame = self.todos_los_frames[Frame_r_n_2]
        l_1 = tk.Label(frame, text=Vector_r, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado de la norma de 3 dimensiones
    def resultado_norma3d(self, x1, x2, x3, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        
        Vector = []

        Vector.append(x1)
        Vector.append(x2)
        Vector.append(x3)
        Vectorint = [int(x) for x in Vector]

        Vectorint = np.array(Vectorint)
        Vector_r = np.linalg.norm(Vectorint)
        Vector_r.tolist()
        
        frame = self.todos_los_frames[Frame_r_n_3]
        l_1 = tk.Label(frame, text=Vector_r, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado de la norma de 4 dimensiones
    def resultado_norma4d(self, x1, x2, x3, x4, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        
        Vector = []

        Vector.append(x1)
        Vector.append(x2)
        Vector.append(x3)
        Vector.append(x4)
        Vectorint = [int(x) for x in Vector]

        Vectorint = np.array(Vectorint)
        Vector_r = np.linalg.norm(Vectorint)
        Vector_r.tolist()
        
        frame = self.todos_los_frames[Frame_r_n_4]
        l_1 = tk.Label(frame, text=Vector_r, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado de la norma de 4 dimensiones
    def resultado_norma5d(self, x1, x2, x3, x4, x5, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        x5 = x5
        
        Vector = []

        Vector.append(x1)
        Vector.append(x2)
        Vector.append(x3)
        Vector.append(x4)
        Vector.append(x5)
        Vectorint = [int(x) for x in Vector]

        Vectorint = np.array(Vectorint)
        Vector_r = np.linalg.norm(Vectorint)
        Vector_r.tolist()
        
        frame = self.todos_los_frames[Frame_r_n_5]
        l_1 = tk.Label(frame, text=Vector_r, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=100)
        frame.tkraise()

    # Muestra el resultado del angulo de 2 dimensiones
    def resultado_angulo2d(self, x1, x2, y1, y2, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        y1 = y1
        y2 = y2
        
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        Producto = np.arccos(np.dot(VectorAint,VectorBint)/(np.linalg.norm(VectorAint)*np.linalg.norm(VectorBint)))
        Producto = np.rad2deg(Producto)
        Producto.tolist()
        
        frame = self.todos_los_frames[Frame_r_a_2]
        l_1 = tk.Label(frame, text=Producto, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del angulo de 3 dimensiones
    def resultado_angulo3d(self, x1, x2, x3, y1, y2, y3, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        y1 = y1
        y2 = y2
        y3 = y3
        
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorA.append(x3)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorB.append(y3)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        Producto = np.arccos(np.dot(VectorAint,VectorBint)/(np.linalg.norm(VectorAint)*np.linalg.norm(VectorBint)))
        Producto = np.rad2deg(Producto)
        Producto.tolist()
        
        frame = self.todos_los_frames[Frame_r_a_3]
        l_1 = tk.Label(frame, text=Producto, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del angulo de 4 dimensiones
    def resultado_angulo4d(self, x1, x2, x3, x4, y1, y2, y3, y4, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        y1 = y1
        y2 = y2
        y3 = y3
        y4 = y4
        
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorA.append(x3)
        VectorA.append(x4)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorB.append(y3)
        VectorB.append(y4)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        Producto = np.arccos(np.dot(VectorAint,VectorBint)/(np.linalg.norm(VectorAint)*np.linalg.norm(VectorBint)))
        Producto = np.rad2deg(Producto)
        Producto.tolist()
        
        frame = self.todos_los_frames[Frame_r_a_4]
        l_1 = tk.Label(frame, text=Producto, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado del angulo de 4 dimensiones
    def resultado_angulo5d(self, x1, x2, x3, x4, x5, y1, y2, y3, y4, y5, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        x5 = x5
        y1 = y1
        y2 = y2
        y3 = y3
        y4 = y4
        y5 = y5
        
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorA.append(x3)
        VectorA.append(x4)
        VectorA.append(x5)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorB.append(y3)
        VectorB.append(y4)
        VectorB.append(y5)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        Producto = np.arccos(np.dot(VectorAint,VectorBint)/(np.linalg.norm(VectorAint)*np.linalg.norm(VectorBint)))
        Producto = np.rad2deg(Producto)
        Producto.tolist()
        
        frame = self.todos_los_frames[Frame_r_a_5]
        l_1 = tk.Label(frame, text=Producto, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado de la distancia de 2 dimensiones
    def resultado_distancia2d(self, x1, x2, y1, y2, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        y1 = y1
        y2 = y2
        
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        distancia = np.linalg.norm(VectorAint-VectorBint)
        distancia.tolist()
        
        frame = self.todos_los_frames[Frame_r_d_2]
        l_1 = tk.Label(frame, text=distancia, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado de la distancia de 3 dimensiones
    def resultado_distancia3d(self, x1, x2, x3, y1, y2, y3, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        y1 = y1
        y2 = y2
        y3 = y3
        
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorA.append(x3)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorB.append(y3)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        distancia = np.linalg.norm(VectorAint-VectorBint)
        distancia.tolist()
        
        frame = self.todos_los_frames[Frame_r_d_3]
        l_1 = tk.Label(frame, text=distancia, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado de la distancia de 4 dimensiones
    def resultado_distancia4d(self, x1, x2, x3, x4, y1, y2, y3, y4, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        y1 = y1
        y2 = y2
        y3 = y3
        y4 = y4
        
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorA.append(x3)
        VectorA.append(x4)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorB.append(y3)
        VectorB.append(y4)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        distancia = np.linalg.norm(VectorAint-VectorBint)
        distancia.tolist()
        
        frame = self.todos_los_frames[Frame_r_d_4]
        l_1 = tk.Label(frame, text=distancia, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

    # Muestra el resultado de la distancia de 5 dimensiones
    def resultado_distancia5d(self, x1, x2, x3, x4, x5, y1, y2, y3, y4, y5, *args, **kwargs):
        
        x1 = x1
        x2 = x2
        x3 = x3
        x4 = x4
        x5 = x5
        y1 = y1
        y2 = y2
        y3 = y3
        y4 = y4
        y5 = y5
        
        VectorA = []
        VectorB = []

        VectorA.append(x1)
        VectorA.append(x2)
        VectorA.append(x3)
        VectorA.append(x4)
        VectorA.append(x5)
        VectorB.append(y1)
        VectorB.append(y2)
        VectorB.append(y3)
        VectorB.append(y4)
        VectorB.append(y5)
        VectorAint = [int(x) for x in VectorA]
        VectorBint = [int(x) for x in VectorB]

        VectorAint = np.array(VectorAint)
        VectorBint = np.array(VectorBint)
        
        distancia = np.linalg.norm(VectorAint-VectorBint)
        distancia.tolist()
        
        frame = self.todos_los_frames[Frame_r_d_5]
        l_1 = tk.Label(frame, text=distancia, font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=1, column=0, padx=150)
        frame.tkraise()

# Frame de eleccion de operación
class Frame_eleccion(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#9A3DBD", )
        

        l_1 = tk.Label(self, text = "Seleccione la operacion a realizar",
        font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=0, column=0, padx=100, pady=10, sticky="w")

        # Calvo
        #self.calvobase = Image.open(r"C:\Users\JORDAN\OneDrive\Documentos\tareas de la uni\Primer semestre\Algebra Lineal\Calculadora de vectores\interfaz\prueba.gif")
        #self.calvo_rszed = self.calvobase.resize((80, 80), Image.Resampling.LANCZOS)
        #self.calvo = ImageTk.PhotoImage(self.calvo_rszed)
        #tk.Label(self, image = self.calvo).place(x=380 , y=80)

        # Radiobutton
        self.seleccion = tk.IntVar()

        estilo_r = ttk.Style()
        estilo_r.configure(".", foreground = "white", background = "#6F218C" ,font=("Comic Sans MS", 10), width = "18")
        
        self.e_v = ttk.Radiobutton(self, text="Escalamiento Vectorial", variable=self.seleccion, value=1)
        self.e_v.grid(row=1, column=0, sticky="n")

        self.p_p = ttk.Radiobutton(self, text="Producto punto", variable=self.seleccion, value=2 )
        self.p_p.grid(row=2, column=0, sticky="n")

        self.norma = ttk.Radiobutton(self, text="Norma", variable=self.seleccion, value=3 )
        self.norma.grid(row=3, column=0, sticky="n")

        self.angulo = ttk.Radiobutton(self, text="Ángulo", variable=self.seleccion, value=4 )
        self.angulo.grid(row=4, column=0, sticky="n")

        self.distancia = ttk.Radiobutton(self, text="Distancia", variable=self.seleccion, value=5)
        self.distancia.grid(row=5, column=0, sticky="n",)


        # Boton de selección de operación
        estilo_B = ttk.Style()
        estilo_B.configure("TButton", background = "purple", foreground = "black", fieldbackground = "purple")
        
        # Seleccionar
        B_seleccionar = ttk.Button(self, text = "Seleccionar", command = lambda:controller.show_frame(self.seleccion.get()))
        B_seleccionar.grid(row=7, column=0, pady=20)


#------------------------------Frame seleccion de dimension de escalamiento de vectores-------------------------------------------------
class Frame_select_dimension_escalamiento(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#9A3DBD")

        l_1 = tk.Label(self, text="Selecciona la dimensión: ")
        l_1.config(font=("Comic Sans MS", 14, "bold"),  background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=0, column=0, padx=100, pady=10, sticky="w")

        # The Rock eyebow 
        #self.therock = Image.open(r"C:\Users\JORDAN\OneDrive\Imágenes\random\InShot_20211209_222013681.gif")
        #self.therock_rszd = self.therock.resize((80, 80), Image.Resampling.LANCZOS)
        #self.therock = ImageTk.PhotoImage(self.therock_rszd)
        #tk.Label(self, image = self.therock).place(x=380 , y=80)

        # RadioButton
        self.s_l = tk.IntVar()

        estilo_r = ttk.Style()
        estilo_r.configure(".", foreground = "white", background = "#6F218C" ,font=("Comic Sans MS", 10))
        self.d_1 = ttk.Radiobutton(self, text="Dos dimensiones", variable=self.s_l, value=1 )
        self.d_1.grid(row=1, column=0, sticky="n")

        self.d_2 = ttk.Radiobutton(self, text="Tres dimensiones", variable=self.s_l, value=2 )
        self.d_2.grid(row=2, column=0, sticky="n")

        self.d_3 = ttk.Radiobutton(self, text="Cuatro dimensiones", variable=self.s_l, value=3 )
        self.d_3.grid(row=3, column=0, sticky="n")

        self.d_4 = ttk.Radiobutton(self, text="Cinco dimensiones", variable=self.s_l, value=4 )
        self.d_4.grid(row=4, column=0, sticky="n")

        # Seleccionar
        B_select_dimension = ttk.Button(self, text="Seleccionar", command= lambda:controller.select_dimension_escalamiento(self.s_l.get()))
        B_select_dimension.grid(row=6, column=0, pady=20)


# Frame de escalmiento vectorial 2 dimensiones
class Frame_escalamiento2(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "blue")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_escalar = tk.StringVar()

        # Entry Vector
        l_1 = tk.Label(self, text=" Ingresa el vector: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        # Entry escalar
        l_2 = tk.Label(self, text="Ingresa el escalar: ")
        l_2.config(font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0)
        
        self.k = tk.Entry(self, textvariable=self.entrada_escalar)
        self.k.focus()
        self.k.grid(row=2, column=1)

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=1, pady=50)

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_escalamiento2d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_escalar.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=3, column=2, pady=50)


# Frame resultado escalamiento 2 dimensiones
class Frame_r_e_2(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_escalamiento2))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de escalmiento vectorial 3 dimensiones
class Frame_escalamiento3(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "blue")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_escalar = tk.StringVar()

        # Entry Vector
        l_1 = tk.Label(self, text=" Ingresa el vector: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3)
        self.x3.focus()
        self.x3.grid(row=1, column=3)

        # Entry escalar
        l_2 = tk.Label(self, text="Ingresa el escalar: ")
        l_2.config(font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0)
        
        self.k = tk.Entry(self, textvariable=self.entrada_escalar)
        self.k.focus()
        self.k.grid(row=2, column=1)

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=1, pady=50)

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_escalamiento3d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get() ,self.entrada_escalar.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=3, column=2, pady=50)


# Frame resultado escalamiento 3 dimensiones
class Frame_r_e_3(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")


        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_escalamiento3))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de escalmiento vectorial 4 dimensiones
class Frame_escalamiento4(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "blue")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()
        self.entrada_escalar = tk.StringVar()

        # Entry Vector
        l_1 = tk.Label(self, text=" Ingresa el vector: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=40)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        # Entry escalar
        l_2 = tk.Label(self, text="Ingresa el escalar: ")
        l_2.config(font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0)
        
        self.k = tk.Entry(self, textvariable=self.entrada_escalar)
        self.k.focus()
        self.k.grid(row=2, column=1)

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=1, pady=50)

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_escalamiento4d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get() ,self.entrada_escalar.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=3, column=2, pady=50)


# Frame resultado escalamiento 4 dimensiones
class Frame_r_e_4(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es:", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_escalamiento4))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de escalmiento vectorial 5 dimensiones
class Frame_escalamiento5(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "blue")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()
        self.entrada_vector_x5 = tk.StringVar()
        self.entrada_escalar = tk.StringVar()

        # Entry Vector
        l_1 = tk.Label(self, text=" Ingresa el vector: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=40)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        self.x5 = tk.Entry(self, textvariable=self.entrada_vector_x5, width=10)
        self.x5.focus()
        self.x5.grid(row=1, column=3, sticky="w")

        # Entry escalar
        l_2 = tk.Label(self, text="Ingresa el escalar: ")
        l_2.config(font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0)
        
        self.k = tk.Entry(self, textvariable=self.entrada_escalar)
        self.k.focus()
        self.k.grid(row=2, column=1)

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=1, pady=50)

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_escalamiento5d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get(), self.entrada_vector_x5.get(), self.entrada_escalar.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=3, column=2, pady=50)


# Frame resultado escalamiento 5 dimensiones
class Frame_r_e_5(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es:", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_escalamiento5))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


#----------------------------------------Frame eleccion de dimension de producto punto-----------------------------------------
class Frame_select_dimension_producto(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#9A3DBD")

        l_1 = tk.Label(self, text="Selecciona la dimensión: ")
        l_1.config(font=("Comic Sans MS", 14, "bold"),  background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=0, column=0, padx=100, pady=10, sticky="w")

        # The Rock eyebow 
        #self.therock = Image.open(r"C:\Users\JORDAN\OneDrive\Imágenes\random\InShot_20211209_222013681.gif")
        #self.therock_rszd = self.therock.resize((80, 80), Image.Resampling.LANCZOS)
        #self.therock = ImageTk.PhotoImage(self.therock_rszd)
        #tk.Label(self, image = self.therock).place(x=380 , y=80)

        # RadioButton
        self.s_l = tk.IntVar()

        estilo_r = ttk.Style()
        estilo_r.configure(".", foreground = "white", background = "#6F218C" ,font=("Comic Sans MS", 10))
        self.d_1 = ttk.Radiobutton(self, text="Dos dimensiones", variable=self.s_l, value=1 )
        self.d_1.grid(row=1, column=0, sticky="n")

        self.d_2 = ttk.Radiobutton(self, text="Tres dimensiones", variable=self.s_l, value=2 )
        self.d_2.grid(row=2, column=0, sticky="n")

        self.d_3 = ttk.Radiobutton(self, text="Cuatro dimensiones", variable=self.s_l, value=3 )
        self.d_3.grid(row=3, column=0, sticky="n")

        self.d_4 = ttk.Radiobutton(self, text="Cinco dimensiones", variable=self.s_l, value=4 )
        self.d_4.grid(row=4, column=0, sticky="n")

        # Seleccionar
        B_select_dimension = ttk.Button(self, text="Seleccionar", command= lambda:controller.select_dimension_producto(self.s_l.get()))
        B_select_dimension.grid(row=6, column=0, pady=20)


# Frame de producto punto de 2 dimensiones
class Frame_producto2(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "aquamarine")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="n")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2)
        self.y2.focus()
        self.y2.grid(row=2, column=2, sticky="n")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_producto2d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado producto 2 dimensiones
class Frame_r_p_2(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_producto2))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de producto punto de 3 dimensiones
class Frame_producto3(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "aquamarine")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()
        self.entrada_vector_y3 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3)
        self.x3.focus()
        self.x3.grid(row=1, column=3)

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="n")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2)
        self.y2.focus()
        self.y2.grid(row=2, column=2, sticky="n")

        self.y3 = tk.Entry(self, textvariable=self.entrada_vector_y3)
        self.y3.focus()
        self.y3.grid(row=2, column=3, sticky="n")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_producto3d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get(), self.entrada_vector_y3.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado producto 3 dimensiones
class Frame_r_p_3(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_producto3))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de producto punto de 4 dimensiones
class Frame_producto4(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "aquamarine")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()
        self.entrada_vector_y3 = tk.StringVar()
        self.entrada_vector_y4 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1, width=11)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="nw")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2, width=10)
        self.y2.focus()
        self.y2.grid(row=2, column=1, sticky="ne")

        self.y3 = tk.Entry(self, textvariable=self.entrada_vector_y3, width=11)
        self.y3.focus()
        self.y3.grid(row=2, column=2, sticky="nw")

        self.y4 = tk.Entry(self, textvariable=self.entrada_vector_y4, width=10)
        self.y4.focus()
        self.y4.grid(row=2, column=2, sticky="ne")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_producto4d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get(), self.entrada_vector_y3.get(), self.entrada_vector_y4.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado producto 4 dimensiones
class Frame_r_p_4(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_producto4))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de producto punto de 5 dimensiones
class Frame_producto5(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "aquamarine")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()
        self.entrada_vector_x5 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()
        self.entrada_vector_y3 = tk.StringVar()
        self.entrada_vector_y4 = tk.StringVar()
        self.entrada_vector_y5 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        self.x5 = tk.Entry(self, textvariable=self.entrada_vector_x5, width=10)
        self.x5.focus()
        self.x5.grid(row=1, column=3, sticky="w")

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1, width=11)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="nw")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2, width=10)
        self.y2.focus()
        self.y2.grid(row=2, column=1, sticky="ne")

        self.y3 = tk.Entry(self, textvariable=self.entrada_vector_y3, width=11)
        self.y3.focus()
        self.y3.grid(row=2, column=2, sticky="nw")

        self.y4 = tk.Entry(self, textvariable=self.entrada_vector_y4, width=10)
        self.y4.focus()
        self.y4.grid(row=2, column=2, sticky="ne")

        self.y5 = tk.Entry(self, textvariable=self.entrada_vector_y5, width=10)
        self.y5.focus()
        self.y5.grid(row=2, column=3, sticky="nw")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_producto5d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get(), self.entrada_vector_x5.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get(), self.entrada_vector_y3.get(), self.entrada_vector_y4.get(), self.entrada_vector_y5.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado producto 5 dimensiones
class Frame_r_p_5(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_producto5))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


#----------------------------------------Frame eleccion de dimension de norma-----------------------------------------
class Frame_select_dimension_norma(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#9A3DBD")

        l_1 = tk.Label(self, text="Selecciona la dimensión: ")
        l_1.config(font=("Comic Sans MS", 14, "bold"),  background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=0, column=0, padx=100, pady=10, sticky="w")

        # The Rock eyebow 
        #self.therock = Image.open(r"C:\Users\JORDAN\OneDrive\Imágenes\random\InShot_20211209_222013681.gif")
        #self.therock_rszd = self.therock.resize((80, 80), Image.Resampling.LANCZOS)
        #self.therock = ImageTk.PhotoImage(self.therock_rszd)
        #tk.Label(self, image = self.therock).place(x=380 , y=80)

        # RadioButton
        self.s_l = tk.IntVar()

        estilo_r = ttk.Style()
        estilo_r.configure(".", foreground = "white", background = "#6F218C" ,font=("Comic Sans MS", 10))
        self.d_1 = ttk.Radiobutton(self, text="Dos dimensiones", variable=self.s_l, value=1 )
        self.d_1.grid(row=1, column=0, sticky="n")

        self.d_2 = ttk.Radiobutton(self, text="Tres dimensiones", variable=self.s_l, value=2 )
        self.d_2.grid(row=2, column=0, sticky="n")

        self.d_3 = ttk.Radiobutton(self, text="Cuatro dimensiones", variable=self.s_l, value=3 )
        self.d_3.grid(row=3, column=0, sticky="n")

        self.d_4 = ttk.Radiobutton(self, text="Cinco dimensiones", variable=self.s_l, value=4 )
        self.d_4.grid(row=4, column=0, sticky="n")

        # Seleccionar
        B_select_dimension = ttk.Button(self, text="Seleccionar", command= lambda:controller.select_dimension_norma(self.s_l.get()))
        B_select_dimension.grid(row=6, column=0, pady=20)


# Frame de norma 2 dimensiones
class Frame_norma2(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#91D51B")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()

        # Entry Vector
        l_1 = tk.Label(self, text=" Ingresa el vector: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=1, pady=50)

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_norma2d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=3, column=2, pady=50)


# Frame resultado norma 2 dimensiones
class Frame_r_n_2(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=170, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_norma2))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=20)


# Frame de norma 3 dimensiones
class Frame_norma3(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#91D51B")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()

        # Entry Vector
        l_1 = tk.Label(self, text=" Ingresa el vector: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3)
        self.x3.focus()
        self.x3.grid(row=1, column=3)

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=1, pady=50)

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_norma3d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=3, column=2, pady=50)


# Frame resultado norma 3 dimensiones
class Frame_r_n_3(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=170, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_norma3))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=20)


# Frame de norma 4 dimensiones
class Frame_norma4(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#91D51B")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()

        # Entry Vector
        l_1 = tk.Label(self, text=" Ingresa el vector: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=1, pady=50)

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_norma4d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=3, column=2, pady=50)


# Frame resultado norma 4 dimensiones
class Frame_r_n_4(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=170, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_norma4))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=20)


# Frame de norma 5 dimensiones
class Frame_norma5(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#91D51B")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()
        self.entrada_vector_x5 = tk.StringVar()

        # Entry Vector
        l_1 = tk.Label(self, text=" Ingresa el vector: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        self.x5 = tk.Entry(self, textvariable=self.entrada_vector_x5, width=10)
        self.x5.focus()
        self.x5.grid(row=1, column=3, sticky="w")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=1, pady=50)

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_norma5d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get(), self.entrada_vector_x5.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=3, column=2, pady=50)

        
# Frame resultado norma 5 dimensiones
class Frame_r_n_5(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=170, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_norma5))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=20)


#----------------------------------------Frame eleccion de dimension de angulo-----------------------------------------
class Frame_select_dimension_angulo(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#9A3DBD")

        l_1 = tk.Label(self, text="Selecciona la dimensión: ")
        l_1.config(font=("Comic Sans MS", 14, "bold"),  background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=0, column=0, padx=100, pady=10, sticky="w")

        # The Rock eyebow 
        #self.therock = Image.open(r"C:\Users\JORDAN\OneDrive\Imágenes\random\InShot_20211209_222013681.gif")
        #self.therock_rszd = self.therock.resize((80, 80), Image.Resampling.LANCZOS)
        #self.therock = ImageTk.PhotoImage(self.therock_rszd)
        #tk.Label(self, image = self.therock).place(x=380 , y=80)

        # RadioButton
        self.s_l = tk.IntVar()

        estilo_r = ttk.Style()
        estilo_r.configure(".", foreground = "white", background = "#6F218C" ,font=("Comic Sans MS", 10))
        self.d_1 = ttk.Radiobutton(self, text="Dos dimensiones", variable=self.s_l, value=1 )
        self.d_1.grid(row=1, column=0, sticky="n")

        self.d_2 = ttk.Radiobutton(self, text="Tres dimensiones", variable=self.s_l, value=2 )
        self.d_2.grid(row=2, column=0, sticky="n")

        self.d_3 = ttk.Radiobutton(self, text="Cuatro dimensiones", variable=self.s_l, value=3 )
        self.d_3.grid(row=3, column=0, sticky="n")

        self.d_4 = ttk.Radiobutton(self, text="Cinco dimensiones", variable=self.s_l, value=4 )
        self.d_4.grid(row=4, column=0, sticky="n")

        # Seleccionar
        B_select_dimension = ttk.Button(self, text="Seleccionar", command= lambda:controller.select_dimension_angulo(self.s_l.get()))
        B_select_dimension.grid(row=6, column=0, pady=20)


# Frame de angulo de 2 dimensiones
class Frame_angulo2(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#DFAF0C")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="n")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2)
        self.y2.focus()
        self.y2.grid(row=2, column=2, sticky="n")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_angulo2d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado angulo 2 dimensiones
class Frame_r_a_2(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_angulo2))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de producto angulo de 3 dimensiones
class Frame_angulo3(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#DFAF0C")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()
        self.entrada_vector_y3 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3)
        self.x3.focus()
        self.x3.grid(row=1, column=3)

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="n")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2)
        self.y2.focus()
        self.y2.grid(row=2, column=2, sticky="n")

        self.y3 = tk.Entry(self, textvariable=self.entrada_vector_y3)
        self.y3.focus()
        self.y3.grid(row=2, column=3, sticky="n")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_angulo3d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get(), self.entrada_vector_y3.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado angulo 3 dimensiones
class Frame_r_a_3(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_angulo3))
        B_regresar.config(font=("Comic Sans MS", 10), width=18)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de angulo de 4 dimensiones
class Frame_angulo4(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#DFAF0C")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()
        self.entrada_vector_y3 = tk.StringVar()
        self.entrada_vector_y4 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1, width=11)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="nw")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2, width=10)
        self.y2.focus()
        self.y2.grid(row=2, column=1, sticky="ne")

        self.y3 = tk.Entry(self, textvariable=self.entrada_vector_y3, width=11)
        self.y3.focus()
        self.y3.grid(row=2, column=2, sticky="nw")

        self.y4 = tk.Entry(self, textvariable=self.entrada_vector_y4, width=10)
        self.y4.focus()
        self.y4.grid(row=2, column=2, sticky="ne")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_angulo4d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get(), self.entrada_vector_y3.get(), self.entrada_vector_y4.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado angulo 4 dimensiones
class Frame_r_a_4(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_angulo4))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de angulo de 5 dimensiones
class Frame_angulo5(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#DFAF0C")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()
        self.entrada_vector_x5 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()
        self.entrada_vector_y3 = tk.StringVar()
        self.entrada_vector_y4 = tk.StringVar()
        self.entrada_vector_y5 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        self.x5 = tk.Entry(self, textvariable=self.entrada_vector_x5, width=10)
        self.x5.focus()
        self.x5.grid(row=1, column=3, sticky="w")

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1, width=11)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="nw")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2, width=10)
        self.y2.focus()
        self.y2.grid(row=2, column=1, sticky="ne")

        self.y3 = tk.Entry(self, textvariable=self.entrada_vector_y3, width=11)
        self.y3.focus()
        self.y3.grid(row=2, column=2, sticky="nw")

        self.y4 = tk.Entry(self, textvariable=self.entrada_vector_y4, width=10)
        self.y4.focus()
        self.y4.grid(row=2, column=2, sticky="ne")

        self.y5 = tk.Entry(self, textvariable=self.entrada_vector_y5, width=10)
        self.y5.focus()
        self.y5.grid(row=2, column=3, sticky="nw")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_angulo5d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get(), self.entrada_vector_x5.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get(), self.entrada_vector_y3.get(), self.entrada_vector_y4.get(), self.entrada_vector_y5.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado angulo 5 dimensiones
class Frame_r_a_5(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_angulo5))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


#----------------------------------------Frame eleccion de dimension de distancia-----------------------------------------
class Frame_select_dimension_distancia(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#9A3DBD")

        l_1 = tk.Label(self, text="Selecciona la dimensión: ")
        l_1.config(font=("Comic Sans MS", 14, "bold"),  background="#6F218C", foreground="#2DAEDA")
        l_1.grid(row=0, column=0, padx=100, pady=10, sticky="w")

        # The Rock eyebow 
        #self.therock = Image.open(r"C:\Users\JORDAN\OneDrive\Imágenes\random\InShot_20211209_222013681.gif")
        #self.therock_rszd = self.therock.resize((80, 80), Image.Resampling.LANCZOS)
        #self.therock = ImageTk.PhotoImage(self.therock_rszd)
        #tk.Label(self, image = self.therock).place(x=380 , y=80)

        # RadioButton
        self.s_l = tk.IntVar()

        estilo_r = ttk.Style()
        estilo_r.configure(".", foreground = "white", background = "#6F218C" ,font=("Comic Sans MS", 10))
        self.d_1 = ttk.Radiobutton(self, text="Dos dimensiones", variable=self.s_l, value=1 )
        self.d_1.grid(row=1, column=0, sticky="n")

        self.d_2 = ttk.Radiobutton(self, text="Tres dimensiones", variable=self.s_l, value=2 )
        self.d_2.grid(row=2, column=0, sticky="n")

        self.d_3 = ttk.Radiobutton(self, text="Cuatro dimensiones", variable=self.s_l, value=3 )
        self.d_3.grid(row=3, column=0, sticky="n")

        self.d_4 = ttk.Radiobutton(self, text="Cinco dimensiones", variable=self.s_l, value=4 )
        self.d_4.grid(row=4, column=0, sticky="n")

        # Seleccionar
        B_select_dimension = ttk.Button(self, text="Seleccionar", command= lambda:controller.select_dimension_distancia(self.s_l.get()))
        B_select_dimension.grid(row=6, column=0, pady=20)


# Frame de distancia de 2 dimensiones
class Frame_distancia2(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#E74C3C")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="n")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2)
        self.y2.focus()
        self.y2.grid(row=2, column=2, sticky="n")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_distancia2d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado distancia 2 dimensiones
class Frame_r_d_2(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_distancia2))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de producto distancia de 3 dimensiones
class Frame_distancia3(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#E74C3C")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()
        self.entrada_vector_y3 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1)
        self.x1.focus()
        self.x1.grid(row=1, column=1)

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2)
        self.x2.focus()
        self.x2.grid(row=1, column=2)

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3)
        self.x3.focus()
        self.x3.grid(row=1, column=3)

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="n")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2)
        self.y2.focus()
        self.y2.grid(row=2, column=2, sticky="n")

        self.y3 = tk.Entry(self, textvariable=self.entrada_vector_y3)
        self.y3.focus()
        self.y3.grid(row=2, column=3, sticky="n")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_distancia3d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get(), self.entrada_vector_y3.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado distancia 3 dimensiones
class Frame_r_d_3(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_distancia3))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de distancia de 4 dimensiones
class Frame_distancia4(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#E74C3C")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()
        self.entrada_vector_y3 = tk.StringVar()
        self.entrada_vector_y4 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1, width=11)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="nw")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2, width=10)
        self.y2.focus()
        self.y2.grid(row=2, column=1, sticky="ne")

        self.y3 = tk.Entry(self, textvariable=self.entrada_vector_y3, width=11)
        self.y3.focus()
        self.y3.grid(row=2, column=2, sticky="nw")

        self.y4 = tk.Entry(self, textvariable=self.entrada_vector_y4, width=10)
        self.y4.focus()
        self.y4.grid(row=2, column=2, sticky="ne")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_distancia4d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get(), self.entrada_vector_y3.get(), self.entrada_vector_y4.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado distancia 4 dimensiones
class Frame_r_d_4(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_distancia4))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


# Frame de distancia de 5 dimensiones
class Frame_distancia5(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#E74C3C")

        self.entrada_vector_x1 = tk.StringVar()
        self.entrada_vector_x2 = tk.StringVar()
        self.entrada_vector_x3 = tk.StringVar()
        self.entrada_vector_x4 = tk.StringVar()
        self.entrada_vector_x5 = tk.StringVar()
        
        self.entrada_vector_y1 = tk.StringVar()
        self.entrada_vector_y2 = tk.StringVar()
        self.entrada_vector_y3 = tk.StringVar()
        self.entrada_vector_y4 = tk.StringVar()
        self.entrada_vector_y5 = tk.StringVar()

        # Entry Vector A
        l_1 = tk.Label(self, text=" Ingresa el vector A: ")
        l_1.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_1.grid(row=1, column=0, sticky="w", padx=10, pady=30)
        
        self.x1 = tk.Entry(self, textvariable=self.entrada_vector_x1, width=11)
        self.x1.focus()
        self.x1.grid(row=1, column=1, sticky="w")

        self.x2 = tk.Entry(self, textvariable=self.entrada_vector_x2, width=10)
        self.x2.focus()
        self.x2.grid(row=1, column=1, sticky="e")

        self.x3 = tk.Entry(self, textvariable=self.entrada_vector_x3, width=11)
        self.x3.focus()
        self.x3.grid(row=1, column=2, sticky="w")

        self.x4 = tk.Entry(self, textvariable=self.entrada_vector_x4, width=10)
        self.x4.focus()
        self.x4.grid(row=1, column=2, sticky="e")

        self.x5 = tk.Entry(self, textvariable=self.entrada_vector_x5, width=10)
        self.x5.focus()
        self.x5.grid(row=1, column=3, sticky="w")

        # Entry Vector B
        l_2 = tk.Label(self, text=" Ingresa el vector B: ")
        l_2.config( font=("Comic Sans MS", 10) ,width=15, background="aquamarine")
        l_2.grid(row=2, column=0, sticky="n")

        self.y1 = tk.Entry(self, textvariable=self.entrada_vector_y1, width=11)
        self.y1.focus()
        self.y1.grid(row=2, column=1, sticky="nw")

        self.y2 = tk.Entry(self, textvariable=self.entrada_vector_y2, width=10)
        self.y2.focus()
        self.y2.grid(row=2, column=1, sticky="ne")

        self.y3 = tk.Entry(self, textvariable=self.entrada_vector_y3, width=11)
        self.y3.focus()
        self.y3.grid(row=2, column=2, sticky="nw")

        self.y4 = tk.Entry(self, textvariable=self.entrada_vector_y4, width=10)
        self.y4.focus()
        self.y4.grid(row=2, column=2, sticky="ne")

        self.y5 = tk.Entry(self, textvariable=self.entrada_vector_y5, width=10)
        self.y5.focus()
        self.y5.grid(row=2, column=3, sticky="nw")

        # Regresar
        B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_eleccion))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=2, column=1, pady=50, sticky="s")

        # Calcular
        B_calcular = tk.Button(self, text="Calcular", command= lambda:[controller.resultado_distancia5d(self.entrada_vector_x1.get(), self.entrada_vector_x2.get(), self.entrada_vector_x3.get(), self.entrada_vector_x4.get(), self.entrada_vector_x5.get(), self.entrada_vector_y1.get(), self.entrada_vector_y2.get(), self.entrada_vector_y3.get(), self.entrada_vector_y4.get(), self.entrada_vector_y5.get())])
        B_calcular.config(font=("Comic Sans MS", 10), width=15)
        B_calcular.grid(row=2, column=2, pady=50, sticky="s")


# Frame resultado distancia 5 dimensiones
class Frame_r_d_5(tk.Frame):
    def __init__(self, container ,controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg= "#9A3DBD")
        
        l_2 = tk.Label(self, text="El resultado es: ", font=("Comic Sans MS", 14, "bold"), background="#6F218C", foreground="#2DAEDA")
        l_2.grid(row=0, column=0, padx=200, pady=20, columnspan= 2, sticky="w")

        # Regresar
        B_regresar = B_regresar = tk.Button(self, text="Regresar", command= lambda:controller.show_frame(Frame_distancia5))
        B_regresar.config(font=("Comic Sans MS", 10), width=15)
        B_regresar.grid(row=3, column=0, pady=50)


#Pdst: no recuerdo como era la luz del sol :'c

root = calculadora()
root.resizable(0,0)

root.mainloop()