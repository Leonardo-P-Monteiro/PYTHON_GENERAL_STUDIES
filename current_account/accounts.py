import abc

class Account(abc.ABC):

    def __init__(self, agency: int, number_account: int, balance: float =0) -> \
    None:
        self._agency = agency
        self._number = number_account
        self._balance = balance
    
    @abc.abstractmethod
    def draw(self, value: float) -> float:
        ...

    def deposit(self, value: float) -> float:
        self._balance += value
        self.details(f'It was deposited: {value:.2f}')
        return self._balance


    def details(self, messager: str ='') -> None:
        print(f'Account balance is {self._balance:.2f}. {messager}')
        print('--'*3)
    
    def __repr__(self):
        class_name = type(self).__name__
        attributes = f'{self._agency!r}, {self._number!r}, {self._balance!r}'
        return f'{class_name}({attributes})'


class SavingsAccount(Account):
    
    def draw(self, value):
        value_after_draw = self._balance - value
        
        if value_after_draw >= 0:
            self._balance -= value
            self.details(f'This value was drawn {value}')
            return self._balance

        print(f"Isn't possible draw value indicated ({value}). You don't have balance enough")
        self.details(f'Neged draw: {value}')
        return self._balance


class CurrentAccount(Account):
    
    def __init__(self, agency, number_account, balance = 0, limit = 0):
        super().__init__(agency, number_account, balance)
        self._limit = limit
    
    def draw(self, value):
        value_after_draw = self._balance - value
        limit_account = -self._limit
        
        if value_after_draw >= limit_account:
            self._balance -= value
            self.details(f'This value was drawn {value}')
            return self._balance

        print(f"Isn't possible draw value indicated ({value}). You don't have balance enough")
        print(f'Your limit is {limit_account:.2f}')
        self.details(f'Neged draw: {value}')
    
    def __repr__(self):
        class_name = type(self).__name__
        attributes = f'{self._agency!r}, {self._number!r}, {self._balance!r}, {self._limit!r}'
        return f'{class_name}({attributes})'


if __name__ == '__main__':
    # cp1 = SavingsAccount( 1, 1)
    # cp1.details()
    # cp1.draw(150.5)
    # cp1.deposit(150)
    # print('-/'*6)
    cc1 = CurrentAccount( 2, 2, 100, 200)
    cc1.details()
    cc1.draw(150.5)
    cc1.deposit(30)
    print(cc1)