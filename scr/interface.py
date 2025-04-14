from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3 

# Conexão com o banco
conne = sqlite3.connect("Stock.db")
cursor = conne.cursor()

# Criação da tabela, se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS vidros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vidro TEXT NOT NULL,
    cor TEXT NOT NULL,
    caixas INTEGER NOT NULL,
    unidade INTEGER NOT NULL
)
""")
conne.commit()

# Função de envio
def send():
    glas = glass.get()
    colo = color.get()
    quanti = quantity.get()
    mul = multiplied.get()

    if not glas or not colo or not quanti or not mul:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    try:
        total = int(quanti) * int(mul)
    except ValueError:
        messagebox.showerror("Erro", "Caixas e Vezes devem ser números")
        return
    
    cursor.execute("INSERT INTO vidros (vidro, cor, caixas, unidade) VALUES (?, ?, ?, ?)", 
                   (glas, colo, quanti, total))
    conne.commit()
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

    # Limpa os campos
    glass.set("")
    color.set("")
    quantity.set("")
    multiplied.set("")

# Janela principal
root = Tk()
root.geometry('450x350')
root.title('Controle de Estoque')

# Variáveis
glass = StringVar()
color = StringVar()
quantity = StringVar()
multiplied = StringVar()

# Notebook (Abas)
abas = ttk.Notebook(root)
abas.pack(fill="both", expand=True)

# Aba 1 - Cadastro
aba1 = Frame(abas)
abas.add(aba1, text="Cadastro")

Label(aba1, text='Tipo de vidro:', font=('Coustard', 10, 'bold')).grid(row=0, column=0, pady=10, padx=5, sticky='e')
Entry(aba1, textvariable=glass).grid(row=0, column=1)

Label(aba1, text='Cor :', font=('Coustard', 10, 'bold')).grid(row=1, column=0, pady=10, padx=5, sticky='e')
Entry(aba1, textvariable=color).grid(row=1, column=1)

Label(aba1, text='Caixas :', font=('Coustard', 10, 'bold')).grid(row=2, column=0, pady=10, padx=5, sticky='e')
Entry(aba1, textvariable=quantity).grid(row=2, column=1)

Label(aba1, text='Vezes :', font=('Coustard', 10, 'bold')).grid(row=3, column=0, pady=10, padx=5, sticky='e')
Entry(aba1, textvariable=multiplied).grid(row=3, column=1)

Button(aba1, text='Enviar', font=('Coustard', 10, 'bold'), command=send).grid(row=4, column=1, pady=20)

# Aba 2 - Retirada (ainda em branco para você usar)
aba2 = Frame(abas)
abas.add(aba2, text="Retirada")
Label(aba2, text="Tela de Retirada", font=('Coustard', 12)).pack(pady=30)

# Aba 3 - Estoque (ainda em branco para você usar)
aba3 = Frame(abas)
abas.add(aba3, text="Estoque")
Label(aba3, text="Visualizar Estoque", font=('Coustard', 12)).pack(pady=30)

root.mainloop()
conne.close()
