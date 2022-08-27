import tkinter as tk
from tkinter import ttk
from crudProduto import crudProduto


janela = tk.Tk()
janelaCrudProduto = crudProduto(janela)
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("720x600+10+10")
janela.mainloop()