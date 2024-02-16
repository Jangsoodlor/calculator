"""UI module for calculator"""
import tkinter as tk
from tkinter import ttk
from tkinter import font
from keypad import Keypad
from display import Display
from historybox import HistoryBox

class CalculatorUI(tk.Tk):
    """UI for calculator"""
    def __init__(self):
        super().__init__()
        self.output = tk.StringVar()
        self.title('Calc')
        self.init_components()

    def bind_keypad(self, caller):
        self.num_pad.bind('<Button>', caller)
        self.fun_box.bind('<<ComboboxSelected>>', caller)

    def init_components(self):
        """init components"""
        options = {'fill': 'both', 'expand':True}
        math_func = ['exp', 'log10', 'ln', 'log2', 'sqrt', 'factorial',
                     'sin', 'cos', 'tan', 'ceil', 'floor']
        logic_operators = [' and ', ' or ', ' not ', '==', '<', '>', '<=', '>=']

        self.history_box = HistoryBox(self)
        self.fun_box = ttk.Combobox(self, values=math_func+logic_operators)
        self.display = Display(self)
        self.default_font = font.nametofont('TkDefaultFont')
        self.default_font.configure(family='Arial', size=20, weight='bold')
        self.num_pad= Keypad(self, ['(',')','DEL','CLS',
                                    'pi', '**', '%', '/',
                                    '7', '8', '9', '*',
                                    '4', '5', '6', '+',
                                    '1', '2', '3', '-',
                                    'e', '0', '.', '='], columns=4)

        self.display.math_operators = ['(',')','**','%','*', '/','+','-','=']
        self.display.fun = math_func

        self.history_box.pack(side='top', **options)
        self.display.pack(side='top', **options)
        self.fun_box.pack(fill='both')
        self.num_pad.pack(**options, side='left')

if __name__ == "__main__":
    calc = CalculatorUI()
    calc.run()
