from calculator_ui import CalculatorUI
from model import Model
from controller import Controller
if __name__ == '__main__':
    controller = Controller(CalculatorUI(), Model())
    controller.run()
