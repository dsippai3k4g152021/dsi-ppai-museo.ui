from tkinter import Frame


class PantallaSede:

    def act_cant_visitantes(self,root):
        self.frame = Frame(root, width=480, height=320)
        self.frame.pack(fill='both', expand=1)
        self.frame.config(bg="yellow")