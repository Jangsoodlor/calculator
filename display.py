"""Display component for calculator"""
from math import *
import tkinter as tk
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

class Display(tk.Label):
    """The display for the calculator"""
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
            if len(self.current_input) == 0 or\
            self.current_input[-1] in self.math_operators:
                self.current_input.extend([f"{val}("])

            else:
                left = [f"{val}("]
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
        if self.current_input:
            self.current_input.pop()
            self.update()

    def calculate(self):
        """calculates the result if possible"""
        if self['fg'] == 'red':
            self['fg'] = 'yellow'
        for i, val in enumerate(self.current_input):
            if val == 'ln':
                self.current_input[i] = 'log'
        self.update()
        self.current_input = [f"{(eval(self['text'])):.5G}"]
        self.update()

    def error(self):
        """notice the user if the calculation is invalid."""
        self['fg'] = 'red'
        pygame.mixer.init()
        pygame.mixer.Sound('invalid_input_noise.mp3').play()

if __name__ == '__main__':
    options = {'fg': 'yellow'}
    root = tk.Tk()
    dp = Display(**options)
    dp.math_operators = ['(',')','**','%','*', '/','+','-','=']
    dp.fun = ['sqrt']
    dp.input('2')
    dp.input('sqrt')
    dp.pack(fill='both', expand=True)
    root.mainloop()
