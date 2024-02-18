from calculator_ui import CalculatorUI
from model import Model
from controller import Controller
if __name__ == '__main__':
    view = CalculatorUI()
    model = Model()
    controller = Controller(view, model)
    controller.run()
