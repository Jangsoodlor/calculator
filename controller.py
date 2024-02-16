from calculator_ui import CalculatorUI
from model import Model

class Controller:
    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model
        self.view.bind_keypad(self.keypad_listener)

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
            self.model.update(before, after)
        except Exception as e:
            self.view.display.error(e)

    def run(self):
        self.view.mainloop()

if __name__ == '__main__':
    controller = Controller(CalculatorUI(), Model())
    controller.run()
