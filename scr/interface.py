from tkinter import *
from tkinter import ttk






root = Tk()
root.geometry('350x350')
root.title('Cadastro')

#craeting the tkinter interface

Label(root, text='Type of Glass').grid(row=2, column=1, pady=10, padx=5)
Entry(root).grid(row=2, column=2)

Label(root, text='Color').grid(row=3, column=1)
Entry(root).grid(row=3, column=2)





root.mainloop()