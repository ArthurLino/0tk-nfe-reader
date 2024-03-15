import tkinter.filedialog
from tkinter import *
from tkinter import ttk

from reader import Reader


def generate(path):
    new_reader = Reader(path=path)
    while len(new_reader.files):
        new_reader.read_nfe_products()
    new_reader.show_total_measurement()


def select_files():
    files = tkinter.filedialog.askopenfile(mode='r').name.split("/")[:-1]
    selected_file = '/'.join(files)
    selected_file_var.set(selected_file)
    print(selected_file)
    return selected_file


root = Tk()
root.title("Levantamento de soma das notas")

content = ttk.Frame(root, height=480, width=320, padding=16)
content.grid()

lbl = Label(content, text="Selecione os arquivos .xml das notas:", pady=12)
lbl.grid(column=1, row=1, columnspan=3)

selected_file = []
selected_file_var = StringVar(value=selected_file)

files_list = Listbox(content, listvariable=selected_file_var)
files_list.grid(column=2, row=2, columnspan=1, rowspan=3)

btn_select = Button(content, text="Selecionar", command=select_files)
btn_select.grid(column=4, row=2, columnspan=1)

btn_generate = Button(content, text="Gerar EXCEL", command=lambda: generate(path=select_files()))
btn_generate.grid(column=4, row=3, columnspan=1)

root.mainloop()
