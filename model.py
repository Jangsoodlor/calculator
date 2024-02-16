"""A Model module"""
class Model:
    """A Model class. It manages the calculator's history database"""
    def __init__(self) -> None:
        self.history = []

    def update(self, calculation:str, result:str):
        """update the history"""
        self.history.append(calculation+' = '+result)

    def get(self, string:str, choice:str=''):
        """returns either the equation or answer based on choice parameter"""
        to_return = self.history[self.history.index(string)]
        for i in range(1, len(to_return)):
            if to_return[i] == '=' \
            and to_return[i-1] == ' ' and to_return[i+1] == ' ':
                equal_sign = i
        if choice == 'equation':
            return to_return[:equal_sign-1]
        return to_return[-(len(to_return)-equal_sign)+2:]

if __name__ == '__main__':
    model = Model()
    X = '9+149-8120-8129382'
    Y = '92212190382190'
    model.update(X, Y)
    print(model.history)
    print(model.get(f'{X} = {Y}', 'equation'))
