import tkinter as tk
from tkinter import messagebox
#creacion de la ventana
app = tk.Tk()
app.title("Calculadora IMC (Praktika)")
app.geometry("600x500")
app.resizable(False, False)

#cosos dentro de la ventana
titulo = tk.Label(app, text="Calculadora de IMC", font=("arial","16","bold"))
titulo.pack(pady=20)
tituloPeso = tk.Label(app, text="Ingrese su peso en kg", font=("arial","12","bold"))
tituloPeso.pack()
peso = tk.Entry(app)
peso.pack(pady=10)
#altura
tituloAltura = tk.Label(app, text="Ingrese su altura", font= ("arial","12","bold"))
tituloAltura.pack()
altura = tk.Entry(app)
altura.pack(pady=10)
#funcion calcular IMC
def calcularIMC():
   #Excepciones uwu
   try:
    pesoValor = peso.get()
    pesoFloat = float(pesoValor)   
    alturaValor = altura.get()
    alturaFloat = float(alturaValor)
   except ValueError:
    messagebox.showerror("Error","Por favor ingrese un numero válido")
    return
   #Calculo 
   imc = pesoFloat / alturaFloat ** 2
   resultados.config(text="Su imc es: "+ str(round(imc,1)))
   if imc < 18.5:
     categoria.config(text="Usted está bajo peso")
   elif imc >= 18.5 and imc <= 24.9: 
     categoria.config(text="Usted está en un peso normal") 
   elif imc >= 25 and imc <= 29.9:
     categoria.config(text="Usted tiene sobrepeso")
   else:
     categoria.config(text="Usted tiene obesidad")
#boton
calculo = tk.Button(app, text="Calcular", font=("arial","10","bold"), command=calcularIMC)
calculo.pack(pady=10)
#muestra de resultados
tituloResultado = tk.Label(app, text="Resultados", font=("arial","12","bold"))
tituloResultado.pack(pady=10)
resultados = tk.Label(app, font=("arial","10","bold"))
resultados.pack(pady=10)
categoria = tk.Label(app, font=("arial","10","bold"))
categoria.pack(pady=10)

app.mainloop()