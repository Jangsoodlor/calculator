"""Controller module for calculator"""

class Controller:
    """The controller module. It manipulates the display and history."""
    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model
        self.view.bind_keypad(self.keypad_listener)
        self.view.history_box.bind_left_click(self.get_equation)
        self.view.history_box.bind_right_click(self.get_answer)

    def keypad_listener(self, event):
        """listen to keypress and call the responsible functions"""
        key = event.widget['text'] or event.widget.get()
        if key == '=':
            self.calculate()
        elif key == 'CLR':
            self.view.display.clear()
        elif key == 'DEL':
            self.view.display.delete()
        else:
            self.view.display.input(key)

    def calculate(self):
        """calculates the result if the input is valid, otherwise play sound and
        change display foreground to red."""
        try:
            before = self.view.display['text']
            self.view.display.calculate()
            after = self.view.display['text']
            self.update_history(before, after)
        except Exception:
            self.view.display.error()

    def update_history(self, before, after):
        """update the history if a valid calculation is successfully calculated."""
        self.model.update(before, after)
        self.view.history_box.update(self.model.history)

    def get_equation(self, event):
        """returns the equation if the user double-click the history"""
        try:
            x = self.view.history_box.get_selection()
            self.view.display.current_input = [self.model.get(x, 'equation')]
            self.view.display.update()
        except Exception:
            self.view.history_box.error()

    def get_answer(self, event):
        """returns the answer if the user right-click the history."""
        try:
            x = self.view.history_box.get_selection()
            self.view.display.current_input = [self.model.get(x)]
            self.view.display.update()
        except Exception:
            self.view.history_box.error()

    def run(self):
        """run the calculator"""
        self.view.mainloop()
