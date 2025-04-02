from tkinter import *
from tkinter import ttk


#creating the functions
def send(self):
    self.glas = glass.get
    self.colo = color.get
    self.quanti = quantity.get
    




root = Tk()
root.geometry('350x350')
root.title('Cadastro')


#creating variables
 
glass = StringVar()
color = StringVar()
quantity = StringVar()
multiplied = StringVar()



#craeting the tkinter interface

Label(root, text='Type of Glass' ).grid(row=2, column=1, pady=10, padx=5)
Entry(root).grid(row=2, column=2)

Label(root, text='Color ').grid(row=3, column=1, pady=1, padx=5)
Entry(root).grid(row=3, column=2)

Label(root, text='Box quantity ').grid(row=4, column=1, pady=10, padx=5)
Entry(root).grid(row=4, column=2)

Label(root, text='Multiplied :').grid(row=5, column=1, pady=10, padx=5)
Entry(root).grid(row=5, column=2)

Button(root, text='To send 📤').grid(row=6, column=2, padx=10, pady=10)




root.mainloop()