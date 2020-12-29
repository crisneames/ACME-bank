import os


# acctid, fname, lname, password, checking bal, savings bal
# 10001;suresh;sigera;juagw362;1000;10000

#

class Customer:

    def __init__(self, bank, account_id=None):
        self.account_id = account_id
        self.bank = bank

    def login(self):
        account_id = input("Account id: ")
        print(self.bank.data[account_id])


class Bank:
    def __init__(self):

        self.data = self.fd()

    def fd(self):

        data = {}

        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'bank.csv')
        file = open(file_path, "r")

        for line in file:
            # print(line)
            column = line.split(';')  # creates column at commas
            # print(column)
            column = [i.strip() for i in column]
            data[column[0]] = column[1:]

        print(data)
        return data

    def add_new_customer(self):

        print("Create user account")
        customer_list = [input(f'Enter first name: '),
                         input(f'Enter last name: '),
                         input(f'Enter password: '),
                         input('(S)avings Account: .'),
                         input('(C)hecking Account: ')]

        self.data['11111'] = customer_list
        self.update_file()
        print(self.data)

    def update_file(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'bank.csv')
        file = open(file_path, "w")

        for key, value in self.data.items():
            file.write(f'{key};{";".join(value)}\n')
        file.close()


"""
class Customer_checking:

    def __init__(self, account_id, password, balance=0):
        self.account_id = account_id
        self.password = password
        self.balance = balance
        print('Welcome to ACME Banking')
        input('(C)hecking or (S)avings Account?')
        # if 'C':
        #     Customer_checking()
        #     elif:
        #         if 'S':
        #             Customer_savings()
        # else:
        #     print("Enter C for Checking Account or S for Savings Account")

    def add_new_customer(self, account_id, first_name, last_name, password):

        print("Create user account")
        self.first_name = input(f'Enter first name: ')
        self.last_name = input(f'Enter last name: ')
        self.password = input(f'Enter password: ')
        self.s_account_type = input('(S)avings Account: .')
        self.c_account_type = input('(C)hecking Account: ')

    def withdraw_money(self):

        amount = float(input("Enter amount to be withdrawn: ")
        if self.balance >= amount:
            self.balance -= amount
            print(f'Withdrawal equals {amount}')
            print(f'Balance equals {self.balance}')
        else:
            print("Not enough funds ")
            print(f'Balance equals {self.balance}')

    def deposit_money(self):

        dep_amount=float(input("Enter amount to be deposited: "))
        self.balance += dep_amount
        print(f'Amount deposited is {dep_amount}')


class Customer_savings(Customer_checking):
    pass


class Login:

    def __init__(self, account_id=None, password=None)

     # if there is no acct, show error msg
       if not get(self.account_id):
            print('No account id')
        else:
            # check if card number has the correct user password
            if password == password:
                # self.welcome_user(BankATM.users[card_number]['username'])
                self.__record=BankATM.users.get(card_number)
                self.welcome_user(self.__record["username"])
            else:
                print('incorrect card number or pin')

    def welcome_user(self, username):
        print(f'welome {username}')


checking=Customer_checking(12325, 2323)
checking.withdraw_money()
"""


def main():
    """

    """

    test1 = Bank()
    test1.add_new_customer()
    customer1 = Customer(test1)
    customer1.login()
    # display_single_record()


# the driver code
if __name__ == '__main__':
    main()
