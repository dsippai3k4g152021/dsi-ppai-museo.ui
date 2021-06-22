from tkinter import Frame, Label


class ImpresoraEntradas:
    frame = None
    label = None

    def imprimir(self, root):
        self.frame = Frame(root, width=480, height=320)
        self.frame.pack(fill='both', expand=1)
        self.frame.config(bg="yellow")
        self.label = Label(self.frame, text="ImpresoraEntradas")
        self.label.place(relx=0.0, rely=1.0, anchor='sw')