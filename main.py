# This is a sample Python script.
from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from interfaz.ImpresoraEntradas import ImpresoraEntradas
from interfaz.PantallaEntrada import PantallaEntrada
from interfaz.PantallaSede import PantallaSede
from interfaz.PantallaVentaEntrada import PantallaVentaEntrada


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def registrarVtaEntrada():
    PantallaVentaEntrada().tomar_op_venta_entradas(root)

def mostrarPantallaEntrada():
    PantallaEntrada().act_cant_visitantes(root)

def mostrarPantallaSede():
    PantallaSede().act_cant_visitantes(root)

def mostrarPantallaImpresora():
    ImpresoraEntradas().imprimir(root)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    root.title("Museo")
    root.geometry("709x698")
    menubar = Menu(root)
    root.config(menu=menubar)
    mainMenu = Menu(menubar,tearoff=0)
    vtaEntradaMenu = Menu(menubar,tearoff=0)
    mostrarmenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Principal", menu=mainMenu)
    mainMenu.add_command(label="Cerrar")
    mainMenu.add_separator()
    mainMenu.add_command(label="Salir", command=root.quit)

    menubar.add_cascade(label="Entrada", menu=vtaEntradaMenu)
    vtaEntradaMenu.add_command(label="Registrar", command=registrarVtaEntrada)

    menubar.add_cascade(label="Mostrar Pantalla", menu=mostrarmenu)
    mostrarmenu.add_command(label="Entrada", command=mostrarPantallaEntrada)
    mostrarmenu.add_command(label="Sede", command=mostrarPantallaSede)
    mostrarmenu.add_command(label="Impresor", command=mostrarPantallaImpresora)


    menubar.add_cascade(label="Ayuda", menu=helpmenu)
    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...")

    #raiz.iconbitmap("form.ico")
    root.mainloop()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
