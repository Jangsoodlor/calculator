"""A module that make keypads"""
import tkinter as tk

class Keypad(tk.Frame):
    """The keypad class"""

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        options = {'sticky': tk.NSEW, 'padx':2, 'pady': 2}
        for i ,keynames in enumerate(self.keynames):
            row = i//columns
            column = i % columns
            button = tk.Button(self, text=keynames)
            button.grid(row=row, column=column, **options)
            self.rowconfigure(row, weight=1)
            self.columnconfigure(column, weight=1)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        for child in self.children.values():
            child.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for child in self.children.values():
            child[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return list(self.children.values())[0][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for child in self.children.values():
            child.configure(cnf, **kwargs)

    @property
    def frame(self):
        """returns a reference to the superclass of the keypad"""
        return super()

if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]
    root = tk.Tk()
    frm = tk.Frame(root)
    root.title("Keypad Demo")
    keypad = Keypad(frm, keynames=keys, columns=3)
    keypad['foreground'] = 'red'
    print(keypad['foreground'])
    keypad.bind('<Button>', lambda x: print(x.widget['text']))
    keypad.frame.configure(background='blue')
    keypad.configure(background='green')
    keypad.pack()
    frm.pack()
    root.mainloop()
