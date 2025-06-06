import tkinter as tk
from tkinter import messagebox
from models.conectar_db import conectar_db
from models.verificar_login import verificar_login
from models.cadastrar_usuario import cadastrar_usuario
from utils.gerar_certificado import gerar_certificado
from models.cadastrar_produto import cadastrar_produto
from models.listagem_produtos import listagem_produtos
from models.editar_produto import editar_produto
from models.apagar_produto import apagar_produto
from utils.gerar_relatorio_db import gerar_relatorio_db

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Login/Cadastro")
        self.tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def tela_login(self):
        self.limpar_tela()
        tk.Label(self.root, text="Login").pack()
        tk.Label(self.root, text="Usuário").pack()
        self.usuario_login = tk.Entry(self.root)
        self.usuario_login.pack()
        
        tk.Label(self.root, text="Senha").pack()
        self.senha_login = tk.Entry(self.root, show="*")
        self.senha_login.pack()
        tk.Button(self.root, text="Entrar", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Cadastrar", command=self.tela_cadastro).pack()
        
    def tela_logado(self):
        self.limpar_tela()
        tk.Label(self.root, text=f"Bem-vindo, {self.nome_usuario}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Cadastrar novo produto", command=self.tela_cadastro_produto).pack(pady=10)
        tk.Button(self.root, text="Listar todos produtos", command=self.tela_listagem_produtos).pack(pady=10)
        tk.Button(self.root, text="Editar produto", command=self.tela_editar_produto).pack(pady=10)
        tk.Button(self.root, text="Apagar produto", command=self.tela_apagar_produto).pack(pady=10)
        tk.Button(self.root, text="Gerar PDF", command=self.tela_gerar_certificado).pack(pady=10)
        tk.Button(self.root, text="Gerar Relatório", command=self.tela_gerar_relatorio).pack(pady=10)
        tk.Button(self.root, text="Sair", command=self.tela_login).pack(pady=10)

        

    def tela_cadastro(self):
        self.limpar_tela()
        tk.Label(self.root, text="Cadastro").pack()
        tk.Label(self.root, text="Usuário").pack()
        self.usuario_cadastro = tk.Entry(self.root)
        self.usuario_cadastro.pack()
        tk.Label(self.root, text="Nome").pack()
        self.nome_cadastro = tk.Entry(self.root)
        self.nome_cadastro.pack()
        tk.Label(self.root, text="Senha").pack()
        self.senha_cadastro = tk.Entry(self.root, show="*")
        self.senha_cadastro.pack()
        tk.Button(self.root, text="Cadastrar", command=self.cadastrar).pack(pady=5)
        tk.Button(self.root, text="Voltar", command=self.tela_login).pack()
    
    def tela_cadastro_produto(self):
        self.limpar_tela()
        tk.Label(self.root, text="Cadastro").pack()
        tk.Label(self.root, text="Produto").pack()
        self.produto_nome = tk.Entry(self.root)
        self.produto_nome.pack()
        tk.Label(self.root, text="Tipo").pack()
        self.produto_tipo = tk.Entry(self.root)
        self.produto_tipo.pack()
        tk.Label(self.root, text="Fornecedor").pack()
        self.produto_fornecedor = tk.Entry(self.root)
        self.produto_fornecedor.pack()
        tk.Label(self.root, text="Preço").pack()
        self.produto_preco = tk.Entry(self.root)
        self.produto_preco.pack()
        tk.Label(self.root, text="Quantidade").pack()
        self.produto_quantidade = tk.Entry(self.root)
        self.produto_quantidade.pack()
        tk.Button(self.root, text="Cadastrar Produto", command=self.cadastrar_produto).pack(pady=5)
        tk.Button(self.root, text="Voltar", command=self.tela_logado).pack()
    
    def tela_listagem_produtos(self):
        self.limpar_tela()
        tk.Label(self.root, text="Listagem de Produtos").pack()
        tk.Label(self.root, text="Produtos cadastrados:").pack()
        produtos = listagem_produtos()
        if produtos:
            for produto in produtos:
                tk.Label(self.root, text=f"Nome: {produto[1]}, Tipo: {produto[2]}, Fornecedor: {produto[3]}, Preço: {produto[4]}, Quantidade: {produto[5]}").pack()
            
        tk.Button(self.root, text="Voltar", command=self.tela_logado).pack(pady=5)
        
    def tela_gerar_certificado(self):
        self.limpar_tela()
        tk.Label(self.root, text="Gerar Certificado").pack()
        tk.Label(self.root, text="Gerar Certificado", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Nome da palestra").pack()
        palestra_entry = tk.Entry(self.root)
        palestra_entry.pack()

        def gerar():
            nome_p = self.nome_usuario
            nome_pal = palestra_entry.get()

            if nome_p and nome_pal:
                arquivo = gerar_certificado(nome_p, nome_pal)
                messagebox.showinfo("Sucesso", f"Certificado salvo como {arquivo}")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos.")
        tk.Button(self.root, text="Gerar Certificado", command=gerar).pack(pady=5)
        tk.Button(self.root, text="Voltar", command=self.tela_logado).pack()
        
    def tela_editar_produto(self):
        self.limpar_tela()
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Editar Produto", font=("Arial", 16)).pack(pady=10)
        tk.Label(frame, text="Selecione o produto a editar:").pack()

        produtos = listagem_produtos()
        self.produto_selecionado = tk.StringVar()
        self.produto_info = {}

        def mostrar_campos_edicao():
            for widget in frame.winfo_children():
                widget.destroy()
            produto_id = self.produto_selecionado.get()
            produto = next((p for p in produtos if str(p[0]) == produto_id), None)
            if produto:
                tk.Label(frame, text="Editar Produto", font=("Arial", 16)).pack(pady=10)
                tk.Label(frame, text="Nome:").pack()
                nome_entry = tk.Entry(frame)
                nome_entry.insert(0, produto[1])
                nome_entry.pack()
                tk.Label(frame, text="Tipo:").pack()
                tipo_entry = tk.Entry(frame)
                tipo_entry.insert(0, produto[2])
                tipo_entry.pack()
                tk.Label(frame, text="Fornecedor:").pack()
                fornecedor_entry = tk.Entry(frame)
                fornecedor_entry.insert(0, produto[3])
                fornecedor_entry.pack()
                tk.Label(frame, text="Preço:").pack()
                preco_entry = tk.Entry(frame)
                preco_entry.insert(0, produto[4])
                preco_entry.pack()
                tk.Label(frame, text="Quantidade:").pack()
                quantidade_entry = tk.Entry(frame)
                quantidade_entry.insert(0, produto[5])
                quantidade_entry.pack()

                def salvar_edicao():
                    novo_nome = nome_entry.get()
                    novo_tipo = tipo_entry.get()
                    novo_fornecedor = fornecedor_entry.get()
                    novo_preco = preco_entry.get()
                    novo_quantidade = quantidade_entry.get()
                    if not (novo_nome and novo_tipo and novo_fornecedor and novo_preco and novo_quantidade):
                        messagebox.showerror("Erro", "Preencha todos os campos.")
                        return
                    try:
                        novo_preco = float(novo_preco)
                        novo_quantidade = int(novo_quantidade)
                    except ValueError:
                        messagebox.showerror("Erro", "Preço deve ser um número e quantidade um inteiro.")
                        return
                    
                    editar_produto(produto[0], novo_nome, novo_tipo, novo_fornecedor, novo_preco, novo_quantidade)
                    messagebox.showinfo("Sucesso", "Produto editado com sucesso!")
                    self.tela_logado()

                tk.Button(frame, text="Salvar", command=salvar_edicao).pack(pady=5)
                tk.Button(frame, text="Cancelar", command=self.tela_logado).pack(pady=5)

        if produtos:
            for produto in produtos:
                tk.Radiobutton(
                    frame,
                    text=f"{produto[1]} - {produto[2]}",
                    variable=self.produto_selecionado,
                    value=produto[0]
                ).pack(anchor=tk.W)
            tk.Button(frame, text="Editar", command=mostrar_campos_edicao).pack(pady=5)
        else:
            tk.Label(frame, text="Nenhum produto cadastrado.").pack()

        tk.Button(frame, text="Voltar", command=self.tela_logado).pack(pady=5)
        
    def tela_apagar_produto(self):
        self.limpar_tela()
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Apagar Produto", font=("Arial", 16)).pack(pady=10)
        tk.Label(frame, text="Selecione o produto a apagar:").pack()

        produtos = listagem_produtos()
        self.produto_selecionado = tk.StringVar()

        if produtos:
            for produto in produtos:
                tk.Radiobutton(
                    frame,
                    text=f"{produto[1]} - {produto[2]}",
                    variable=self.produto_selecionado,
                    value=produto[0]
                ).pack(anchor=tk.W)

            def apagar():
                produto_id = self.produto_selecionado.get()
                if produto_id:
                    if messagebox.askyesno("Confirmar", "Você tem certeza que deseja apagar este produto?"):
                        if apagar_produto(produto_id):
                            messagebox.showinfo("Sucesso", "Produto apagado com sucesso!")
                            self.tela_logado()
                        else:
                            messagebox.showerror("Erro", "Erro ao apagar produto.")
                else:
                    messagebox.showerror("Erro", "Selecione um produto para apagar.")

            tk.Button(frame, text="Apagar Produto", command=apagar).pack(pady=5)
        else:
            tk.Label(frame, text="Nenhum produto cadastrado.").pack()

        tk.Button(frame, text="Voltar", command=self.tela_logado).pack(pady=5)
        
    def tela_gerar_relatorio(self):
        self.limpar_tela()
        tk.Label(self.root, text="Gerar Relatório", font=("Arial", 18)).pack(pady=10)

        def gerar():
            gerar_relatorio_db()
            messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")

        tk.Button(self.root, text="Gerar Relatório", command=gerar).pack(pady=5)
        tk.Button(self.root, text="Voltar", command=self.tela_logado).pack()
        

    def login(self):
        usuario = self.usuario_login.get()
        senha = self.senha_login.get()

        nome = verificar_login(usuario, senha)

        if nome:
            self.nome_usuario = nome  
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.tela_logado()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def cadastrar(self):
        usuario = self.usuario_cadastro.get()
        nome = self.nome_cadastro.get()
        senha = self.senha_cadastro.get()
        if cadastrar_usuario(usuario, nome, senha):
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.tela_login()
        else:
            messagebox.showerror("Erro", "Usuário já existe.")
            
    def cadastrar_produto(self):
        nome = self.produto_nome.get()
        tipo = self.produto_tipo.get()
        fornecedor = self.produto_fornecedor.get()
        preco = self.produto_preco.get()
        quantidade = self.produto_quantidade.get()

        if nome and tipo and fornecedor and preco and quantidade:
            try:
                preco = float(preco)
                quantidade = int(quantidade)
                if cadastrar_produto(nome, tipo, fornecedor, preco, quantidade):
                    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
                    self.tela_logado()
                else:
                    messagebox.showerror("Erro", "Erro ao cadastrar produto.")
            except ValueError:
                messagebox.showerror("Erro", "Preço deve ser um número e quantidade um inteiro.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

if __name__ == "__main__":
    conectar_db()
    root = tk.Tk()
    root.geometry("1920x1080") 
    app = App(root)
    root.mainloop()
