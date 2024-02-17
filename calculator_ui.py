"""UI module for calculator"""
import tkinter as tk
from tkinter import ttk
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
        """binds the keypad"""
        self.num_pad.bind('<Button>', caller)
        self.fun_box.bind('<<ComboboxSelected>>', caller)

    def init_components(self):
        """init components"""
        options = {'fill': 'both', 'expand':True}
        math_func = ['exp', 'log10', 'ln', 'log2', 'sqrt', 'factorial',
                     'sin', 'cos', 'tan', 'ceil', 'floor']
        logic_operators = [' and ', ' or ', ' not ', '==', '<', '>', '<=', '>=']
        history_container = tk.Frame()
        fun_container = tk.Frame()
        self.history_box = HistoryBox(history_container)
        scrollbar = tk.Scrollbar(history_container, orient='vertical',
                                 command=self.history_box.yview)
        self.history_box.config(yscrollcommand=scrollbar.set)
        fun_label = tk.Label(fun_container, text='Select Math Functions here: ')
        self.fun_box = ttk.Combobox(fun_container,
                                    values=math_func+logic_operators)
        self.display = Display(self)
        self.num_pad= Keypad(self, ['(',')','DEL','CLR',
                                    'pi', '**', '%', '/',
                                    '7', '8', '9', '*',
                                    '4', '5', '6', '+',
                                    '1', '2', '3', '-',
                                    'e', '0', '.', '='], columns=4)
        self.display.math_operators = ['(',')','**','%','*', '/','+','-','=']
        self.display.fun = math_func
    
        self.num_pad['font'] = ('Arial', 20)
        self.history_box['font'] = ('Arial' ,12)

        top_label1 = tk.Label(history_container, text='History. Please select equation first,')
        top_label2 = tk.Label(history_container,
                        text='Double-Click to display equation. Right-Click to display answer')
        top_label1.pack(anchor='w', padx=5)
        top_label2.pack(anchor='w', padx=5)
        self.history_box.pack(**options, padx=5, pady=5, side='left')
        scrollbar.pack(side='right', fill='y')
        history_container.pack(**options)
        self.display.pack(side='top', **options)
        fun_label.pack(side='left')
        self.fun_box.pack(side='right', fill=tk.X, expand=True)
        fun_container.pack(**options, padx=5, pady=5)
        self.num_pad.pack(**options, side='left')

if __name__ == "__main__":
    calc = CalculatorUI()
    calc.run()
