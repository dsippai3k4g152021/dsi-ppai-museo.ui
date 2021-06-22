from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

class PantallaVentaEntrada:
    cant_entrada = 0
    combo_tarifas = ''
    entradas = []
    tarifas_seleccionadas = []
    gestor_venta_entrada = None
    frame = None
    tree = None
    label = None

    def __init__(self):
        print("soy una creeper gordita")

    def tomar_op_venta_entradas(self, root):
        self.habilitar_ventana(root)

    def habilitar_ventana(self, root):
        self.frame = Frame(root, width=480, height=320)
        self.frame.pack(fill='both', expand=1)
        self.frame.config(bg="lightblue")
        self.label = Label(self.frame, text="Tarifas vigentes")
        self.label.place(relx=0.0, rely=1.0, anchor='sw')
        columns = ('#1', '#2', '#3', '#4')
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')
        self.tree.place(relx=0.0, rely=0.10, anchor='sw')
        self.tree.heading('#1', text='Tipo Entrada')
        self.tree.heading('#2', text='Tipo Visita')
        self.tree.heading('#3', text='Monto')
        self.tree.heading('#4', text='Guia')
        self.tree.pack(side="top", fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        contacts = []
        for n in range(1, 6):
            contacts.append((f'Entrada {n}', f'Visita {n}', f'${n}', f'${n}' ))

        # adding data to the treeview
        for contact in contacts:
            self.tree.insert('', "end", values=contact)
        self.tree.grid(row=0, column=0, sticky='nsew')

    def mostrar_nombre_apellido_empleado(self):
        pass


    def on_tree_select(self, event):
        for selected_item in self.tree.selection():
            # dictionary
            item = self.tree.item(selected_item)
            # list
            record = item['values']
            #
            showinfo(title='Information',
                     message=','.join(record))
