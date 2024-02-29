import person_client as client
import accounts as count

class Bank:
    
    def __init__(
            self,
            agency: list[int] | None = None,
            account: list[count.Account] | None = None,
            client: list[client.Person] | None = None
            ):
        self.agency = agency or []
        self.account = account or []
        self.client = client or []
    
    def check_agency(self, account: count.Account):
        if account._agency in self.agency:
            print('Check agence is OK')
            return True
        print('Agency is false.')
        return False
    
    def check_client(self, client:client.Person):
        if client in self.client:
            print('Check client bank is OK.')
            return True
        print('Client is false.')
        return False

    def check_account(self, account:count.Account):
        if account in self.account:
            print('Check account is OK')
            return True
        print('Account is false.')
        return False

    def check_belong_account_client(self, client: client.Client, account:count.Account):
        if account is client.account:
            print("Account belong's client.")
            return True
        print("Account don't belong to client")
        return False 
  
    def authentication(self, client: client.Client, account: count.Account):
        return self.check_agency(account) and \
        self.check_client(client) and \
            self.check_account(account) and\
            self.check_belong_account_client(client, account)

    def __repr__(self):
        class_name = __class__.__name__
        attributes = f'{self.agency!r}, {self.account!r}, {self.client!r}'
        return f'{class_name}({attributes})'







if __name__ == '__main__':
    client_1 = client.Client('Leo', 27)
    account_client_1 = count.SavingsAccount(1, 111, 100)
    client_1.account = account_client_1
    bank_1 = Bank()
    bank_1.client.extend([client_1])
    bank_1.account.append(account_client_1)
    bank_1.agency.append(1)

    client_2 = client.Client('Francisco', 19)
    account_client_2 = count.CurrentAccount(2, 214, 1200, 400)
    client_2.account = account_client_2
    bank_1.client.append(client_2)
    bank_1.agency.append(2)
    bank_1.account.append(account_client_2)

    

    # print(bank_1)
    # bank_1.authentication(client_2, account_client_2)
    # print(bank_1.check_account(account_client_1))

    if bank_1.authentication(client_2, account_client_2):
        account_client_2.draw(1300.00)
        account_client_2.draw(400)
        client_2.account.deposit(2000)
        account_client_2.details()
        
