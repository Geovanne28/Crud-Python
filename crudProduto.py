import tkinter as tk
from tkinter import ttk
from ProdutoModel import ProdutoModel

class crudProduto:
    def __init__(self, janela):
        self.janela = janela
        self.banco = ProdutoModel()

        #componentes
        self.lbCodigo=tk.Label(self.janela, text='Código do Produto:')
        self.lblNome=tk.Label(self.janela, text='Nome do Produto')
        self.lblPreco=tk.Label(self.janela, text='Preço')

        self.txtCodigo=tk.Entry(bd=3)
        self.txtNome=tk.Entry()
        self.txtPreco=tk.Entry()        
        self.btnCadastrar=tk.Button(self.janela, text='Cadastrar', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(self.janela, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(self.janela, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(self.janela, text='Limpar', command=self.fLimparTela)

         #Componente TreeView
        self.dadosColunas = ("Código", "Nome", "Preço")
        self.treeProdutos = ttk.Treeview(self.janela,  columns=self.dadosColunas, selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(self.janela, orient="vertical", command=self.treeProdutos.yview)        
        self.verscrlbar.pack(side ='right', fill ='x')
        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        self.treeProdutos.heading("Código", text="Código")
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("Preço", text="Preço")
        self.treeProdutos.column("Código",minwidth=0,width=100)
        self.treeProdutos.column("Nome",minwidth=0,width=100)
        self.treeProdutos.column("Preço",minwidth=0,width=100)
        self.treeProdutos.pack(padx=10, pady=10)
        self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        #posicionamento dos componentes na janela
        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)
        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)
        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)
        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)
        
        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=605, y=300, height=225)        
        self.carregarDadosIniciais()
    
    def carregarDadosIniciais(self):
        try:
            registros = self.banco.select()
            for registro in registros:
                id     = registro[0]
                codigo = registro[1]
                nome   = registro[2]
                preco  = registro[3]
                self.treeProdutos.insert("", "end", iid=id,values=(codigo, nome, preco))
            print('registros',registros)
        except:
            print('Ainda não existem dados para carregar')

    def fCadastrarProduto(self):
        try:
            codigo, nome, preco= self.fLerCampos()
            id = self.banco.insert(codigo, nome, preco)
            self.treeProdutos.insert("", "end", iid=id,values=(codigo, nome, preco))
            self.fLimparTela()
        except:
            print('Não foi possível fazer o cadastro.')

    def fLerCampos(self):
        try:
          codigo = int(self.txtCodigo.get())
          nome=self.txtNome.get()
          preco=float(self.txtPreco.get())
        except:
          print('Não foi possível ler os dados.')

        return codigo, nome, preco

    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeProdutos.selection():  
            item = self.treeProdutos.item(selection)  
            codigo,nome,preco = item["values"][0:3]  
            self.txtCodigo.insert(0, codigo)  
            self.txtNome.insert(0, nome)  
            self.txtPreco.insert(0, preco) 
    
    def fAtualizarProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos()
            id = self.treeProdutos.selection()[0]
            self.banco.update(id, codigo, nome, preco)   
            #recarregar dados na tela
            self.treeProdutos.delete(*self.treeProdutos.get_children()) 
            self.carregarDadosIniciais()
            self.fLimparTela()
        except:
            print('Não foi possível atualizar o registro.')

    def fExcluirProduto(self):
        try:
            id = self.treeProdutos.selection()[0]
            print('id',id)
            self.banco.delete(id)
            self.treeProdutos.delete(*self.treeProdutos.get_children()) 
            self.carregarDadosIniciais()
            self.fLimparTela()
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível excluir o registro.')
    
    
    def fLimparTela(self):
        try:
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
        except:
            print('Não foi possível limpar a tela.')