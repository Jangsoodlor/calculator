from calculator_ui import CalculatorUI

class Controller:
    def __init__(self, view) -> None:
        self.view = view
        self.view.bind_keypad(self.keypad_listener)

    def keypad_listener(self, event):
        key = event.widget['text']
        if key == '=':
            self.calculate()
        else:
            self.view.display.input(key)

    def calculate(self):
        try:
            self.view.display.calculate()
        except Exception as e:
            self.view.display.error(e)

    def run(self):
        self.view.mainloop()

if __name__ == '__main__':
    controller = Controller(CalculatorUI())
    controller.run()