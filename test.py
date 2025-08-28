import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Cadastro de Aluno")
root.geometry("1920x1080")
root.mainloop()

title = tk.Label(root, text="Cadastro de Aluno", font=("Arial", 10))
title.pack(pady=10)

# Criar a barra de menu
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Criar um menu "Arquivo"
menu_arquivo = tk.Menu(barra_menu, tearoff=0)  # tearoff=0 remove a linha tracejada
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)