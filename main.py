import datetime
class Bank:
    ...

class BankAccount:
    def __init__(self, name, initial_balance, dob, acc_num):
        self.name = name
        self.balance = initial_balance
        self.dob = dob
        self.acc_num = acc_num
        self.log = []

    def __int__(self):
        return self.acc_num

    def __str__(self):
        return (f'Account holder: {self.name}\n'
                f'Account number: {self.acc_num}\n'
                f'Account number: {self.balance}')

    def add_money(self, how_much):
        self.balance += how_much
        self.log_event(f'added {how_much}; new balance {self.balance}')

    def withdraw_money(self, how_much):
        self.balance -= how_much
        self.log_event(f'withdrew {how_much}; new balance {self.balance}')

    def transfer_money(self, how_much, where_to):
        self.withdraw_money(how_much)
        where_to.add_money(how_much)

    def check_balance(self):
        ...

    def freeze_account(self):
        ...

    def log_event(self, param):
        self.log.append(
            f'{datetime.datetime.now()}: {param}'
        )


my_account = BankAccount(name='daryl', acc_num=1234, initial_balance=10, dob='19751028')
another_account = BankAccount(name='bob', acc_num=1235, initial_balance=0, dob='19751027')
account_list = [my_account, another_account]
focus_account = my_account
while True:
    if focus_account:
        print(focus_account)
        print('1: Add funds\n'
              '2: Remove funds\n'
              '3: Balance enquiry\n'
              '4: Transfer money\n'
              '5: Manage accounts\n')
        choice = input('Pick one: ')

        if choice == '1':
            how_much = input('How much?')
            focus_account.add_money(float(how_much))
        elif choice == '2':
            how_much = input('How much?')
            focus_account.withdraw_money(float(how_much))
        elif choice == '3':
            print(focus_account.balance)
        elif choice == '4':
            for i in range(len(account_list)):
                print(f'{i}: {account_list[i]}')

            choice = input('Pick one: ')

            dest_account = account_list[int(choice)]

            how_much = input('How much?')

            focus_account.transfer_money(float(how_much), dest_account)

        elif choice == '5':
            focus_account = None
    else:
        print('Account management:\n'
              '1: Select a account\n'
              '2: Add an account\n'
              '3: Delete an account\n')
        choice = input('Pick one')

        if choice == '1':
            for i in range(len(account_list)):
                print(f'{i}: {account_list[i]}')

            choice = input('Pick one: ')

            focus_account = account_list[int(choice)]
