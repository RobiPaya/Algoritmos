import tkinter as tk
from tkinter import ttk
class ListboxFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(
            self,
            xscrollcommand=self.hscrollbar.set,
            yscrollcommand=self.vscrollbar.set
        )
        self.hscrollbar.config(command=self.listbox.xview)
        self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.vscrollbar.config(command=self.listbox.yview)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack()
root = tk.Tk()
root.title("Lista con barras de desplazamiento")
root.geometry("400x300")
listbox_frame = ListboxFrame()
listbox_frame.listbox.insert(
    tk.END,
    *(f"Elemento {i} con un texto muy largo" for i in range(100))
)
listbox_frame.pack()
root.mainloop()