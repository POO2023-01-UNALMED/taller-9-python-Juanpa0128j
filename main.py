from tkinter import Tk, Button, Entry,StringVar

class Calculator(): 
    @classmethod
    def mostrar_num(cls, num):
        if(cls.operator == "="):
            cls.num_mostrar.set(str(num))
        else:
            cls.num_mostrar.set(cls.num_mostrar.get() + str(num))

    @classmethod
    def resultado_mostrar(cls):
        if cls.operator == "suma":
            l = list(cls.num_mostrar.get())
            del l[0 : l.index("+") + 1]
            cls.num_mostrar.set("".join(l))
            cls.num_mostrar.set(cls.result + float(cls.num_mostrar.get()))

        elif cls.operator == "resta":
            l = list(cls.num_mostrar.get())
            del l[0 : l.index("-") + 1]
            cls.num_mostrar.set("".join(l))
            cls.num_mostrar.set(cls.result-float(cls.num_mostrar.get()))

        elif cls.operator == "multiplicación":
            l = list(cls.num_mostrar.get())
            del l[0 : l.index("*") + 1]
            cls.num_mostrar.set("".join(l))
            cls.num_mostrar.set(cls.result*float(cls.num_mostrar.get()))

        elif cls.operator == "división":
            l = list(cls.num_mostrar.get())
            del l[0 : l.index("/") + 1]
            cls.num_mostrar.set("".join(l))
            cls.num_mostrar.set(cls.result/float(cls.num_mostrar.get()))

        cls.result = 0
        cls.operator = "="


    @classmethod
    def suma(cls, num):
        cls.result = float(num)
        cls.num_mostrar.set(cls.num_mostrar.get() + "+")
        cls.operator = "suma"
    
    @classmethod
    def resta(cls, num):
        cls.result = float(num)
        cls.num_mostrar.set(cls.num_mostrar.get() + "-")
        cls.operator = "resta"
    
    @classmethod
    def multiplicacion(cls, num):
        cls.result = float(num)
        cls.num_mostrar.set(cls.num_mostrar.get() + "*")
        cls.operator = "multiplicación"
    
    @classmethod
    def division(cls, num):
        cls.result = float(num)
        cls.num_mostrar.set(cls.num_mostrar.get() + "/")
        cls.operator = "división"

    def __init__(self):
        # Configuración ventana principal
        self.root = Tk()
        self.root.title("Calculadora POO")
        self.root.resizable(0,0)
        self.root.geometry("290x250")
        self.num_mostrar = StringVar()
        Calculator.num_mostrar = self.num_mostrar

        # Configuración self.pantalla de salida 
        self.pantalla = Entry(self.root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"), textvariable=Calculator.num_mostrar)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

        # Configuración botones
        self.boton_1 = Button(self.root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda:Calculator.mostrar_num(1)).grid(row=1, column=0, padx=1, pady=1)
        self.boton_2 = Button(self.root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda:Calculator.mostrar_num(2)).grid(row=1, column=1, padx=1, pady=1)
        self.boton_3 = Button(self.root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda:Calculator.mostrar_num(3)).grid(row=1, column=2, padx=1, pady=1)
        self.boton_4 = Button(self.root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda:Calculator.mostrar_num(4)).grid(row=2, column=0, padx=1, pady=1)
        self.boton_5 = Button(self.root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda:Calculator.mostrar_num(5)).grid(row=2, column=1, padx=1, pady=1)
        self.boton_6 = Button(self.root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda:Calculator.mostrar_num(6)).grid(row=2, column=2, padx=1, pady=1)
        self.boton_7 = Button(self.root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda:Calculator.mostrar_num(7)).grid(row=3, column=0, padx=1, pady=1)
        self.boton_8 = Button(self.root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda:Calculator.mostrar_num(8)).grid(row=3, column=1, padx=1, pady=1)
        self.boton_9 = Button(self.root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda:Calculator.mostrar_num(9)).grid(row=3, column=2, padx=1, pady=1)
        self.boton_igual = Button(self.root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command = lambda:Calculator.resultado_mostrar()).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        self.boton_punto = Button(self.root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command = lambda:Calculator.mostrar_num(".")).grid(row=4, column=2, padx=1, pady=1)
        self.boton_mas = Button(self.root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda:Calculator.suma(Calculator.num_mostrar.get())).grid(row=1, column=3, padx=1, pady=1)
        self.boton_menos = Button(self.root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda:Calculator.resta(Calculator.num_mostrar.get())).grid(row=2, column=3, padx=1, pady=1)
        self.boton_multiplicacion = Button(self.root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda:Calculator.multiplicacion(Calculator.num_mostrar.get())).grid(row=3, column=3, padx=1, pady=1)
        self.boton_division = Button(self.root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda:Calculator.division(Calculator.num_mostrar.get())).grid(row=4, column=3, padx=1, pady=1)

        self.root.mainloop()

    num_mostrar = None
    num_mostrar_aux = None
    result = 0
    operator = ""

if __name__ == "__main__":
    calculator = Calculator()