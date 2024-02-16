import tkinter as tk
from tkinter import messagebox

class HistoryBox(tk.Listbox):
    def __init__(self, master=None, lst=[], **kw):
        super().__init__(master, **kw)
        self['height'] = 2
        self.update(lst)

    def update(self, lst):
        self['listvariable'] = tk.Variable(value=lst)

    def bind_left_click(self, func=None, add=None):
        self.bind('<Double-Button-1>', func, add)

    def bind_right_click(self, func=None, add=None):
        self.bind('<Button-2>', func, add)
        self.bind('<Button-3>', func, add)

    def get_selection(self):
        return self.get(self.curselection())

    def error(self):
        messagebox.showerror('Error', 'Please select an equation first')

if __name__ == '__main__':
    def x(event):
        try:
            print(lb.get(lb.curselection()))
        except Exception:
            pass
    root = tk.Tk()
    lst = [1,2,3]
    lstvar = tk.Variable(value=lst)
    lb = HistoryBox(root, lst, bg='red')
    lb.bind_left_click(x)
    lb.pack()
    root.mainloop()