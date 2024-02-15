"""Display component for calculator"""
import tkinter as tk
from tkinter import messagebox

class Display(tk.Label):
    def __init__(self, master=None, cnf={}, **kwargs):
        super().__init__(master, cnf, **kwargs)
        self.current_input = []
        self.math_operators = []
        self.fun = []
        self.init_components()

    def init_components(self):
        """initialise components"""
        self.configure(font=('Arial', 50),
                    fg='yellow',
                    background='black',
                    anchor='e')

    def update(self):
        """update the based on current input"""
        self['text'] = "".join(self.current_input)

    def input(self, val):
        """update the display when there's a new input"""
        if val in self.fun:
            if self.current_input[-1] in self.math_operators:
                self.current_input.append(val)
                self.current_input.append('(')
            else:
                left = []
                left.append(val)
                left.append('(')
                self.current_input.append(')')
                self.current_input = left+self.current_input
        else:
            self.current_input.append(val)
        self.update()

    def clear(self):
        """clear the display"""
        self.current_input = []
        self.update()

    def delete(self):
        """delete the last thing inputted from the display"""
        self.current_input.pop()
        self.update()

    def calculate(self):
        if self['fg'] == 'red':
            self['fg'] = 'yellow'
        self.current_input = [str(eval(self['text']))]
        self.update()

    def error(self, e):
        self['fg'] = 'red'
        messagebox.showerror('error', e)

if __name__ == '__main__':
    from math import *
    options = {'fg': 'yellow'}
    root = tk.Tk()
    dp = Display(**options)
    dp.math_operators = ['(',')','**','%','*', '/','+','-','=']
    dp.fun = ['sqrt']
    dp.input('2')
    dp.input('sqrt')
    dp.pack(fill='both', expand=True)

    # lst = ['a', 'b', 'c']
    # lstvar = tk.Variable(value=lst)
    # lb = tk.Listbox(root, listvariable=lstvar, height=10, selectmode=tk.SINGLE)
    # lb.bind('<Double-Button-1>', lambda x: print(lb.get(lb.curselection())))
    # lb.pack()

    root.mainloop()
