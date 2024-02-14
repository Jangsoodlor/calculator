"""UI module for calculator"""
import tkinter as tk
from tkinter import font
from keypad import Keypad

class CalculatorUI(tk.Tk):
    """UI for calculator"""
    def __init__(self):
        super().__init__()
        self.output = tk.StringVar()
        self.title('Calc')
        self.init_components()

    def keypress(self, event):
        """Output the key that the user presses on the display"""
        text = event.widget['text']
        self.output.set(self.output.get() + text)

    def init_components(self):
        """init components"""
        options = {'fill': 'both', 'expand':True}
        self.default_font = font.nametofont('TkDefaultFont')
        self.default_font.configure(family='Arial', size=20, weight='bold')
        num_frame = Keypad(self, list('789456123 0.'), columns=3)
        num_frame.bind('<Button>', self.keypress)
        op_frame = Keypad(self, ['*', '/','+','-','^','='], columns=1)
        op_frame.bind('<Button>', self.keypress)
        display = tk.Label(bg='black', fg='yellow',
                           textvariable=self.output, anchor='e', font=('Arial', 50))
        display.pack(side='top', **options, anchor='n')
        num_frame.pack(**options, side='left', anchor='w')
        op_frame.pack(**options, side='right', anchor='e')

    def run(self):
        """keeps the program open"""
        self.mainloop()

if __name__ == "__main__":
    calc = CalculatorUI()
    calc.run()
