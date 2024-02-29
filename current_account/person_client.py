import accounts as count

class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name: str = name
        self._age: int = age

    @property
    def show_name(self):
        return self._name
    
    @show_name.setter
    def edit_name(self, name: str):
        self._name = name
    
    @property
    def show_age(self):
        return self._age
    
    @show_age.setter
    def edit_age(self, age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attributes = f'{self.show_name}, {self.show_age}'
        return f'{class_name}({attributes})'


class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: count.Account | None = None

    # def __repr__(self):
    #     class_name = __class__.__name__
    #     attributes = f'{self._name}, {self._age}'
    #     return f'{class_name}({attributes})'

if __name__ == '__main__':
    c1 = Client('Léo', 27)
    c1.account = count.SavingsAccount(1, 1, 100)
    print(c1)
    print(c1.account)
    c2 = Client('Francisco', 32)
    c2.account = count.CurrentAccount(1, 2, 60, 40)
    print(c2)
    print(c2.account)
 