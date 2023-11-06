from datetime import datetime


class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = self.name+self.email
        self.__balance = 0
        self.transaction_history = []
        self.loan_balance = 0
        self.loan_taken = 0

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print('Invalid Amount!')

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            self.transaction_history.append(
                f'{datetime.now()}, Deposit: {amount}')
            print(f'Deposit Successfully {amount}')
        else:
            print('Invalid Amount !')

    def withdraw(self, amount):
        if admin.isBankrupt == True:
            print('Bankrupt. Users cannot withdraw Money')
        elif amount > 0 and amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            self.transaction_history.append(
                f'{datetime.now()}, Withdraw {amount}')
            print(f'Withdraw Successfully {amount}')
        else:
            print('Withdrawal amount exceeded !.')

    def available_balance(self):
        print(f'Available Balance: {self.get_balance()}')

    def history(self):
        print(self.transaction_history)

    def take_loan(self, amount):
        if admin.isLoan_active == False:
            print('Opps ! Sorry the loan option currently Disable.Try later')
        elif self.loan_taken < 2:
            self.set_balance(self.get_balance() + amount)
            self.loan_taken += 1
            self.loan_balance += amount
            self.transaction_history.append(
                f'{datetime.now()}, Took Loan: {amount}')
            print(
                f'SUccessfully Took Loan {amount} for {self.loan_taken} time')
        else:
            print(f'You already Exceeded loan time limit !.')

    def transfer(self, amount, t_person):
        if admin.isBankrupt == True:
            print('Bankrupt. Users cannot withdraw Money')
        elif t_person is not None and isinstance(t_person, User):
            if amount <= self.get_balance():
                self.set_balance(self.get_balance() - amount)
                t_person.deposit(amount)
                self.transaction_history.append(
                    f'{datetime.now()}, Transfer {amount} to {t_person.name}')
                t_person.transaction_history.append(
                    f'{datetime.now()}, Received {amount} from {self.name}')
                print(f'Successfully Transfer {amount} to {t_person.name}')
            else:
                print('Transfer amount exceeded !.')
        else:
            print(f'{t_person} Account does not exist !')


class Admin:
    def __init__(self) -> None:
        self.__name = 'admin'
        self.__password = '123'
        self.all_users = []
        self.isBankrupt = False
        self.isLoan_active = True

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.all_users.append(user)
        print(f'Create user Successfully for {user.name}')
        return user

    def delete_account(self, user):
        if user in self.all_users:
            self.all_users.remove(user)
            print(f'Successfully removed account for {user.name}')

    def account_list(self):
        return self.all_users

    def total_available_balance(self):
        total = sum(user.get_balance() for user in self.all_users)
        print(f'Bank Total Balance: {total}')

    def total_loan(self):
        total = sum(user.loan_balance for user in self.all_users)
        print(f'Total Loan Amount: {total}')

    def bankrupt_enable(self):
        self.isBankrupt = True

    def bankrupt_disable(self):
        self.isBankrupt = False

    def loan_active_disable(self):
        self.isLoan_active = False

    def loan_active_enable(self):
        self.isLoan_active = True


admin = Admin()
currentUser = None
while True:
    if currentUser == None:
        print('\nNo Logged in User !.')
        op = int(input('As User or Admin ? (1/2): '))
        if op == 1:
            ch = input('\n Logged in or Register ? (L/R): ')
            if ch == 'R':
                print('Give some info for Register as a User !\n')
                name = input('Enter your Name: ')
                email = input('Enter Your Email: ')
                address = input('Enter Your Address: ')
                account_type = input(
                    'Savings or Current ? Type (savings/current): \n')
                user = admin.create_account(name, email, address, account_type)
                currentUser = user

            else:
                no = input("Enter Your Account Number: ")
                for account in admin.all_users:
                    if no == account.account_number:
                        currentUser = account
                        break
                    else:
                        print('Invalid user name or password !')
        else:
            l_name = input('Enter your Name: ')
            l_password = input('Enter your password: ')
            if admin.get_name() == l_name and admin.get_password() == l_password:
                currentUser = admin
            else:
                print('Invalid user name or password !')

    elif currentUser == admin:
        print(f'Welcome Your Options : \n')
        print('1. Create an Account')
        print('2. Delete Account')
        print('3. View all Account')
        print('4. Total available Balance')
        print('5. Total Loan Amount')
        print('6. Bankrupt')
        print('7. Loan Active')
        print('8. Log out')
        opt = input('Enter Your Choice:\n')

        if opt == '1':
            print('Give some info About User ')
            name = input('Enter your Name: ')
            email = input('Enter Your Email: ')
            address = input('Enter Your Address: ')
            account_type = input('Savings or Current ? Type (savings/current)')
            admin.create_account(name, email, address, account_type)

        elif opt == '2':
            ac_no = input('Enter Account number you want to delete: ')
            for user in admin.all_users:
                if ac_no == user.account_number:
                    admin.delete_account(user)

        elif opt == '3':
            print('All Users ! \n')
            for user in admin.account_list():
                print(f'Name; {user.name} No: {user.account_number}\n')

        elif opt == '4':
            print('Total Balance:\n')
            admin.total_available_balance()

        elif opt == '5':
            print('Total Loan:\n')
            admin.total_loan()
        elif opt == '6':
            ch = input('Are Want Bankrupt Enable (y/n): ')
            if ch == 'y':
                admin.bankrupt_enable()
                print('Bankrupt Successfully Enabled !')
            elif ch == 'n':
                admin.bankrupt_disable()
                print('Bankrupt Successfully Disabled !')
        elif opt == '7':
            ch = input('Are Want Loan Disabled (y/n): ')
            if ch == 'y':
                admin.loan_active_disable()
                print('Successfully Disable Loan Option')
            elif ch == 'n':
                admin.loan_active_enable()
                print('Successfully Enable Loan Option')

        elif opt == '8':
            currentUser = None

    else:
        print('\n User Options:\n')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Check Balance')
        print('4. Transaction History')
        print('5. Take Loan')
        print('6. Transfer Money')
        print('7. Log out')

        ch = int(input('Enter your option: \n'))

        if ch == 1:
            amount = int(input('Enter your deposit amount: '))
            currentUser.deposit(amount)
        elif ch == 2:
            amount = int(input('Enter your withdraw amount: '))
            currentUser.withdraw(amount)
        elif ch == 3:
            currentUser.available_balance()
        elif ch == 4:
            currentUser.history()
        elif ch == 5:
            amount = int(input('Enter your loan amount: '))
            currentUser.take_loan(amount)
        elif ch == 6:
            t_person = input(
                'Enter Account Number you want to transfer money to: ')
            amount = int(input('Enter your transfer amount: '))
            receiver = None
            for user in admin.all_users:
                if t_person == user.account_number:
                    receiver = user
                    break
            if receiver is not None:
                currentUser.transfer(amount, receiver)
            else:
                print('Failed: Account not found.')

        elif ch == 7:
            currentUser = None
