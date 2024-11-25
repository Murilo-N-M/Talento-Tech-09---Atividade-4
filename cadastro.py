from carro import Carro
from caminhao import Caminhao
from moto import Moto
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Funções criação obj e lista
lista=[]

def listar(obj):
    lista.append(obj)

def atualizaListBox():
    listbox.delete(0, tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())

def cadastrarAnimal():
    marca = entryMarca.get()
    modelo = entryModelo.get()
    ano = entryAno.get()
    motor = entryMotor.get()
    cavalo = entryCavalos.get()
    nPortas = entryNPortas.get()
    tipo = varTipo.get()

    erro = 0

    if tipo == "Carro":
        if marca == "":
            messagebox.showinfo("Erro", "Marca não informado")
            erro = 1
        elif modelo == "":
            messagebox.showinfo("Erro", "Modelo não informado")
            erro = 1
        elif ano == "":
            messagebox.showinfo("Erro", "Ano não informado")
            erro = 1
        elif motor == "":
            messagebox.showinfo("Erro", "Motor não informado")
            erro = 1
        elif cavalo == "":
            messagebox.showinfo("Erro", "Cavalos não informado")
            erro = 1
        elif nPortas == "":
            messagebox.showinfo("Erro", "N° de portas não informado")
            erro = 1
        else:
            erro = 0
        if erro == 0:
            c = Carro(marca, modelo, ano, motor, cavalo, nPortas)
            listar(c)
            messagebox.showinfo("Cadastrado", "Carro cadastrado com sucesso!")
    elif tipo == "Moto":
        if marca == "":
            messagebox.showinfo("Erro", "Marca não informado")
            erro = 1
        elif modelo == "":
            messagebox.showinfo("Erro", "Modelo não informado")
            erro = 1
        elif ano == "":
            messagebox.showinfo("Erro", "Ano não informado")
            erro = 1
        elif motor == "":
            messagebox.showinfo("Erro", "Motor não informado")
            erro = 1
        elif cavalo == "":
            messagebox.showinfo("Erro", "Cavalos não informado")
            erro = 1
        # elif nPortas == "":
        #     messagebox.showinfo("Erro", "N° de portas não informado")
        #     erro = 1
        else:
            erro = 0
        if erro == 0:
            m = Moto(marca, modelo, ano, motor, cavalo)
            listar(m)
            messagebox.showinfo("Cadastrado", "Moto cadastrada com sucesso!")
    elif tipo == "Caminhão":
        if marca == "":
            messagebox.showinfo("Erro", "Marca não informado")
            erro = 1
        elif modelo == "":
            messagebox.showinfo("Erro", "Modelo não informado")
            erro = 1
        elif ano == "":
            messagebox.showinfo("Erro", "Ano não informado")
            erro = 1
        elif motor == "":
            messagebox.showinfo("Erro", "Motor não informado")
            erro = 1
        elif cavalo == "":
            messagebox.showinfo("Erro", "Cavalos não informado")
            erro = 1
        elif nPortas == "":
            messagebox.showinfo("Erro", "N° de portas não informado")
            erro = 1
        else:
            erro = 0
        if erro == 0:
            cm = Caminhao(marca, modelo, ano, motor, cavalo, nPortas)
            listar(cm)
            messagebox.showinfo("Cadastrado", "Caminhão cadastrado com sucesso!")
#Função das paginas principais
main = tk.Tk()
main.title("Cadastro")
main.geometry("700x400")
main.grid_rowconfigure(0, weight= 1)
main.grid_columnconfigure(0, weight= 1)

janela = ttk.Notebook(main)
janela.grid(row= 0, column= 0, sticky= "nsew")

tab1 = ttk.Frame(janela)
tab1.grid_columnconfigure(0, weight= 1)
tab1.grid_columnconfigure(1, weight= 1)
for i in range(8):
    tab1.grid_rowconfigure(i, weight=1)

tab2 = ttk.Frame(janela)
tab2.grid_columnconfigure(0, weight= 1)
tab2.grid_columnconfigure(1, weight= 1)

janela.add(tab1, text="Cadastro")
janela.add(tab2, text="lista de Veiculos")

#função da pagina cadastro
label1= tk.Label(tab1, text="Marca:", font=("", 15))
label1.grid(row= 0, column= 0, sticky= "w", padx= 10)
entryMarca= tk.Entry(tab1, font=("",15), borderwidth= 3)
entryMarca.grid(row=0, column= 1, sticky= "nsew", padx= 10, pady= 7)

label2= tk.Label(tab1, text="Modelo:", font=("", 15))
label2.grid(row= 1, column= 0, sticky= "w", padx= 10)
entryModelo= tk.Entry(tab1, font=("",15), borderwidth= 3)
entryModelo.grid(row=1, column= 1, sticky= "nsew", padx= 10, pady= 7)

label3= tk.Label(tab1, text="Ano:", font=("", 15))
label3.grid(row= 2, column= 0, sticky= "w", padx= 10)
entryAno= tk.Entry(tab1, font=("",15), borderwidth= 3)
entryAno.grid(row=2, column= 1, sticky= "nsew", padx= 10, pady= 7)

label4= tk.Label(tab1, text="Motor:", font=("", 15))
label4.grid(row= 3, column= 0, sticky= "w", padx= 10)
entryMotor= tk.Entry(tab1, font=("",15), borderwidth= 3)
entryMotor.grid(row=3, column= 1, sticky= "nsew", padx= 10, pady= 7)

label5= tk.Label(tab1, text="Cavalos:", font=("", 15))
label5.grid(row= 4, column= 0, sticky= "w", padx= 10)
entryCavalos= tk.Entry(tab1, font=("",15), borderwidth= 3)
entryCavalos.grid(row=4, column= 1, sticky= "nsew", padx= 10, pady= 7)

label6= tk.Label(tab1, text="N° de portas (Vazio caso 0):", font=("", 15))
label6.grid(row= 5, column= 0, sticky= "w", padx= 10)
entryNPortas= tk.Entry(tab1, font=("",15), borderwidth= 3)
entryNPortas.grid(row=5, column= 1, sticky= "nsew", padx= 10, pady= 7)

varTipo = tk.StringVar(value= "Carro")
label7= tk.Label(tab1, text="Tipo de veiculo:", font=("", 15))
label7.grid(row= 6, column= 0, sticky= "w", padx= 10)
tk.Radiobutton(tab1, text="Carro", font=("", 15),variable=varTipo, value="Carro", borderwidth=3).grid(row=6, column= 1, sticky= "w")
tk.Radiobutton(tab1, text="Moto", font=("", 15),variable=varTipo, value="Moto", borderwidth=3).grid(row=6, column= 1, sticky= "n", padx= 50)
tk.Radiobutton(tab1, text="Caminhão", font=("", 15),variable=varTipo, value="Caminhão", borderwidth=3).grid(row=6, column= 1, sticky= "e")

tk.Button(tab1, text="Cadastrar", font=("", 15), borderwidth=15, command=cadastrarAnimal).grid(row=7, columnspan=2)

#Função da pagina lista
listbox= tk.Listbox(tab2)
listbox.config(font=("", 10), width= 100, height= 17, borderwidth= 1)
listbox.grid(row=0, column=0, sticky="nsew",padx=10, pady=10)
tk.Button(tab2, text="Atualizar", font=("", 15), command=atualizaListBox, borderwidth= 5).grid(row=1, column=0, pady=5)

#Rodar o codigo
main.mainloop()