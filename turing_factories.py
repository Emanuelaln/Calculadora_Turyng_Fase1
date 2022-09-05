import tkinter as tk
from typing import Text

def exemplo():
    rota= tk.Tk()
    rota.title('SOBRE DESENVOLVEDORES')
    rota.configure(padx=10, pady=10,background='0x23a8f2')
    rota.geometry("300x200")
    rota.positionfrom("500")
    tk.Label(text='@Mnuel Dalla',justify='centert',font='5em',background='red')

    rota.mainloop()

def make_root()->tk.Tk:
    root = tk.Tk()
    root.title('Genius-Turing')
    root.configure(padx=10, pady=10,background='#dde')
    root.geometry("600x400")
    root.resizable(False,False)
    my_menu = tk.Menu(root)
    root.config(menu=my_menu)
    file_menu = tk.Menu(my_menu)
    my_menu.add_cascade(label="Ficheiro",menu=file_menu)
    file_menu.add_command(label="Abrir Ficheiro",command=root.quit)
    file_menu.add_command(label="Salvar Ficheiro",command=root.quit)
    file_menu.add_command(label="Nova Expressao Regular",command=root.quit)
    file_menu.add_command(label="Nova Expressao Matematica",command=root.quit)
    file_menu.add_separator()
    file_menu.add_command(label="Sair",command=root.quit)
    edit_menu = tk.Menu(my_menu)
    my_menu.add_cascade(label="Editar",menu=edit_menu)
    edit_menu.add_command(label="Cortar",command=root.quit)
    edit_menu.add_command(label="Copiar & Colar",command=root.quit)
    help_menu = tk.Menu(my_menu)
    my_menu.add_cascade(label="Ajuda",menu=help_menu)
    help_menu.add_command(label="Como Funciona",command=root.quit)
    help_menu.add_command(label="O Nosso Forum Online",command=root.quit)
    dev_menu = tk.Menu(my_menu)
    my_menu.add_cascade(label="Sobre Nos",menu=dev_menu)
    dev_menu.add_command(label="Desenvolvedores",command=exemplo)
    dev_menu.add_command(label="Mais Solucoes da Genius",command=root.quit)
    return root

    def make_labe(root)->tk.Label:
        label=tk.Label(
            root,text="Manuel",
            anchor="e",justify="center",
            background="#fff"
        )
        label.grid(row=0,colum=0,columnspan=5)
        return label
    




