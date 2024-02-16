"""Display component for calculator"""
import tkinter as tk
from tkinter import messagebox
from math import *

class Display(tk.Label):
    def __init__(self, master=None, cnf={}, **kwargs):
        super().__init__(master, cnf, **kwargs)
        self.current_input = []
        self.math_operators = []
        self.fun = []
        self.configure(font=('Arial', 50),
                    fg='yellow',
                    bg='black',
                    anchor='e',
                    pady = 50,
                    padx = 5)

    def update(self):
        """update the based on current input"""
        self['text'] = "".join(self.current_input)

    def input(self, val):
        """update the display when there's a new input"""
        if val in self.fun:
            if len(self.current_input) == 0:
                self.current_input.extend([val, '('])
            elif self.current_input[-1] in self.math_operators:
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
        self.current_input.clear()
        self.update()

    def delete(self):
        """delete the last thing inputted from the display"""
        self.current_input.pop()
        self.update()

    def calculate(self):
        if self['fg'] == 'red':
            self['fg'] = 'yellow'
        for i, val in enumerate(self.current_input):
            if val == 'ln':
                self.current_input[i] = 'log'
        self.update()
        self.current_input = [f"{(eval(self['text'])):.5G}"]
        self.update()

    def error(self, e):
        self['fg'] = 'red'
        messagebox.showerror('Error', e)

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
    root.mainloop()
