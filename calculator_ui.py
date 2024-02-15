"""UI module for calculator"""
import tkinter as tk
from tkinter import ttk
from tkinter import font
from keypad import Keypad
from display import Display

class CalculatorUI(tk.Tk):
    """UI for calculator"""
    def __init__(self):
        super().__init__()
        self.output = tk.StringVar()
        self.title('Calc')
        self.init_components()

    def bind_keypad(self, caller):
        self.num_pad.bind('<Button>', caller)
        self.operator_pad.bind('<Button>', caller)
        self.fun.bind('<<ComboboxSelected>>', caller)

    def init_components(self):
        """init components"""
        options = {'fill': 'both', 'expand':True}
        math_func = ['exp', 'log10', 'ln', 'log2', 'sqrt']
        self.fun = ttk.Combobox(self, values=math_func)
        self.display = Display()
        self.default_font = font.nametofont('TkDefaultFont')
        self.default_font.configure(family='Arial', size=20, weight='bold')
        self.num_pad= Keypad(self, list('789456123 0.'), columns=3)
        self.operator_pad = Keypad(self, ['CLS', 'DEL', '(',')','**','%','*', '/','+','-','=&colspan=2'], columns=2)
        self.display.math_operators = [i['text'] for i in self.operator_pad.children.values()]
        self.display.fun = math_func

        self.display.pack(side='top', **options)
        self.fun.pack(fill='both')
        self.num_pad.pack(**options, side='left')
        self.operator_pad.pack(**options, side='right')

if __name__ == "__main__":
    calc = CalculatorUI()
    calc.run()
