from calculator_ui import CalculatorUI
from model import Model

class Controller:
    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model
        self.view.bind_keypad(self.keypad_listener)
        self.view.history_box.bind_left_click(self.get_equation)
        self.view.history_box.bind_right_click(self.get_answer)

    def keypad_listener(self, event):
        key = event.widget['text'] or event.widget.get()
        if key == '=':
            self.calculate()
        elif key == 'CLS':
            self.view.display.clear()
        elif key == 'DEL':
            self.view.display.delete()
        else:
            self.view.display.input(key)

    def calculate(self):
        try:
            before = self.view.display['text']
            self.view.display.calculate()
            after = self.view.display['text']
            self.update_history(before, after)
        except Exception as e:
            self.view.display.error(e)

    def update_history(self, before, after):
        self.model.update(before, after)
        self.view.history_box.update(self.model.history)

    def get_equation(self, event):
        try:
            x = (self.view.history_box.get_selection())
            self.view.display.current_input = [self.model.get(x, 'equation')]
            self.view.display.update()
        except Exception:
            self.view.history_box.error()

    def get_answer(self, event):
        try:
            x = (self.view.history_box.get_selection())
            self.view.display.current_input = [self.model.get(x)]
            self.view.display.update()
        except Exception:
            self.view.history_box.error()

    def run(self):
        self.view.mainloop()

if __name__ == '__main__':
    controller = Controller(CalculatorUI(), Model())
    controller.run()
