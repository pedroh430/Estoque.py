from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3 


# Conexão com o banco
conne = sqlite3.connect("Stock")
cursor = conne.cursor()


#enviar os dados
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
    
    # Conexão com o banco
    conne = sqlite3.connect("Stock")
    cursor = conne.cursor()
    
    cursor.execute("INSERT INTO vidros (vidro, cor, caixas, unidade) VALUES (?, ?, ?, ?)", 
                   (glas, colo, quanti, total))
    conne.commit()
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

    # Limpa os campos
    glass.set("")
    color.set("")
    quantity.set("")
    multiplied.set("")
    
    show_itens()
    

def retirar_unidades():
    glas = glass.get()
    colo = color.get()
    try:
        units = int(quantity.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para unidades")
        return

    if not glas or not colo:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    # Buscar a quantidade atual no banco de dados
    cursor.execute("SELECT unidade FROM vidros WHERE vidro = ? AND cor = ?", (glas, colo))
    result = cursor.fetchone()
    
    if result:
        current_unit = result[0]
        new_units = current_unit - units

        if new_units < 0:
            messagebox.showerror("Erro", "Quantidade insuficiente no estoque")
        elif new_units == 0:
            # Remove o item se a unidade for zero
            cursor.execute("DELETE FROM vidros WHERE vidro = ? AND cor = ?", (glas, colo))
            conne.commit()
            messagebox.showinfo("Removido", f"Todas as unidades de {glas} ({colo}) foram removidas do estoque.")
        else:
            # Atualiza com a nova quantidade
            cursor.execute("UPDATE vidros SET unidade = ? WHERE vidro = ? AND cor = ?", (new_units, glas, colo))
            conne.commit()
            messagebox.showinfo("Sucesso", f"{units} unidades retiradas. Nova quantidade: {new_units}")
    else:
        messagebox.showerror("Erro", "Item não encontrado no banco de dados")

    # Limpa os campos
    glass.set("")
    color.set("")
    quantity.set("")
    
    show_itens()
    
    
    
def show_itens():
    for row in tree.get_children():
        tree.delete(row)
    
    cursor.execute("SELECT vidro, cor, caixas, unidade FROM vidros")
    registros = cursor.fetchall()

    for registro in registros:
        tree.insert("", "end", values=registro)

    
    

# Janela principal
root = Tk()
root.geometry('450x300')
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

Label(aba1, text='Tipo de vidro:', font=('Coustard', 12, 'bold')).grid(row=0, column=0, pady=10, padx=5)
Entry(aba1, textvariable=glass).grid(row=0, column=1)

Label(aba1, text='Cor :', font=('Coustard', 12, 'bold')).grid(row=1, column=0, pady=10, padx=5, sticky='e')
Entry(aba1, textvariable=color).grid(row=1, column=1)

Label(aba1, text='Caixas :', font=('Coustard', 12, 'bold')).grid(row=2, column=0, pady=10, padx=5, sticky='e')
Entry(aba1, textvariable=quantity).grid(row=2, column=1)

Label(aba1, text='Vezes :', font=('Coustard', 12, 'bold')).grid(row=3, column=0, pady=10, padx=5, sticky='e')
Entry(aba1, textvariable=multiplied).grid(row=3, column=1)

Button(aba1, text='Enviar', font=('Coustard', 12, 'bold'), command=send).grid(row=4, column=1, pady=20)

# Aba 2 - Retirada 
aba2 = Frame(abas)
abas.add(aba2, text="Retirada")
# titulo
Label(aba2, text="Retirar itens",font=('Coustard', 12, 'bold') ).grid(row=0,column=1)

Label(aba2, text="Tipo de vidro", font=('Coustard', 12, 'bold')).grid(row=1, column= 0, pady= 10, padx= 5  )
Entry(aba2, textvariable= glass ).grid(row=1, column=1)



Label(aba2, text="Digite a cor", font=('Coustard', 12, 'bold')).grid(row=2, column= 0, pady= 10, padx= 5  )
Entry(aba2, textvariable= color ).grid(row=2, column=1)

Label(aba2, text=" digite a quantidade", font=('Coustard', 12, 'bold')). grid(row=3 , column=0, pady=10, padx= 5)
Entry(aba2, textvariable=quantity).grid(row=3, column=1)


Button(aba2, text='Enviar', font=('Coustard', 12, 'bold'), command=retirar_unidades).grid(row=4, column=1, pady=20)



# Aba 3 - Estoque 
aba3 = Frame(abas)
abas.add(aba3, text="Estoque")

coluns = ("vidro","cor","caixas","unidades" )
tree = ttk.Treeview(aba3, columns= coluns, show="headings")
tree.pack(padx=20, pady=10, fill="both", expand=True)

for colu in coluns:
    tree.heading(colu, text=colu)
    tree.column(colu, width =100)



Button(aba3, text="listar", command=show_itens).pack(pady=10)


root.mainloop()
conne.close()
