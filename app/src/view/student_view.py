# Este arquivo contém a interface gráfica do usuário (GUI).

import tkinter as tk
from tkinter import ttk

class StudentView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Cadastro de Alunos")
        self.create_widgets()

    def create_widgets(self):
        # ... Crie os widgets da interface gráfica aqui ...
        # Por exemplo, campos de entrada e botões

    def mainloop(self):
        self.root.mainloop()