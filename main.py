import time 
import tkinter as tk
from tkinter import *
from tkinter import ttk

#Controladores do cronometro
cronometro_status = False

def iniciar_cronometro():
    global cronometro_inicio, cronometro_status
    cronometro_inicio = time.time()
    cronometro_status = True
    cronometro()

def parar_cronometro():
    global cronometro_status
    cronometro_status = False


#Função Principal, atualiza o valor de tempo_PassadoDisplay
def cronometro():
    if cronometro_status:
        tempo_Passado = time.time() - cronometro_inicio
        tempo_PassadoDisplay.set(f"{tempo_Passado:.2f} segundos")
        window.after(10, cronometro)


#Setando a GUI
window = Tk()
window.geometry("420x420")
window.title("Cronometro")


#Formatação do tempo_Passado para que possa ser lido pelo Tkinter
tempo_PassadoDisplay = tk.StringVar()
tempo_PassadoDisplay.set("0.00 segundos")


#Elementos da GUI
label = ttk.Label(window, textvariable=tempo_PassadoDisplay, font=("Helvetica", 24))
label.pack(pady=20)

Botao_iniciar = ttk.Button(window, text="Iniciar", command=iniciar_cronometro)
Botao_iniciar.pack()

Botao_iniciar = ttk.Button(window, text="Parar", command=parar_cronometro)
Botao_iniciar.pack()


#Chamando a GUI e a função cronometro
window.after(10, cronometro)
window.mainloop()