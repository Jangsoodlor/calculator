from calculator_ui import CalculatorUI

class Controller:
    def __init__(self, view) -> None:
        self.view = view
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
        print(self.view.display.current_input)

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