"""UI module for calculator"""
import tkinter as tk
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

    def init_components(self):
        """init components"""
        options = {'fill': 'both', 'expand':True}
        self.display = Display()
        self.default_font = font.nametofont('TkDefaultFont')
        self.default_font.configure(family='Arial', size=20, weight='bold')
        num_pad= Keypad(self, list('789456123 0.'), columns=3)
        operator_pad = Keypad(self, ['(',')','**','%','*', '/','+','-','=&colspan=2'], columns=2)

        self.display.pack(side='top', **options)
        num_pad.pack(**options, side='left')
        operator_pad.pack(**options, side='right')

    def run(self):
        """keeps the program open"""
        self.mainloop()

if __name__ == "__main__":
    calc = CalculatorUI()
    calc.run()
