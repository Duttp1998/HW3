class Account:
    def __init__(self, name, acct_num):
        self.name = name
        self.acct_num = acct_num

    def withdraw(self, amount):
        print('Withdrawing amount for ', self.acct_num)

    def deposit(self, amount):
        print('Depositing amount for ', self.acct_num)

class PrivilegedAccount(Account):
    def scheduleAppointment(self):
        print('Scheduling appointment for ', self.acct_num)

#PrivilegedAccount class object
pa = PrivilegedAccount('Ian', 1001)
pa.withdraw(100)
pa.deposit(500)
pa.scheduleAppointment()