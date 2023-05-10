class BankAccount:
    """A Regular bank account"""
    def __init__(self, initial_balance=0) -> None:
        self._balance = initial_balance
    
    def __repr__(self) -> str:
        ## __mro__ -> (tuple of class names in the full inheritance chain leading up to object)
        instance_name = "".join([i.__name__ for i in type(self).__mro__[:-1]])
        return f'A {instance_name} with ${self._balance} in it.'

    @property
    def balance(self):
        return self._balance
    
    def isPositive(self, value):
        if not value > 0:
            raise ValueError('Only positive value is available!')

        return value

    ## Only support transactions in positive amounts.
    def deposit(self, value):
        if self.isPositive(value):
            self._balance += value

            print(f'Deposited ${value:.2f}.')
            
    ## Only support transactions in positive amounts.
    def withdraw(self, value):
        if self.isPositive(value):
            self._balance -= value

            print(f'Withdrew ${value}.')
    
class Savings(BankAccount):
    """Like a bank account but interest-earning"""
    interest = .0035
    
    # def __repr__(self) -> str:
    #     return f'A SavingAccount with ${self.balance:.2f} in it.'
    
    def pay_interest(self):
        interest_earned = self.balance * self.interest

        self.deposit(interest_earned)

class HighInterest(Savings):
    """Like a Saving account but earning higher interest, in exchange for withdrawal fee"""

    interest = .007
    
    ## it is taken from the account's balance on every withdrawal.
    def __init__(self, withdrawal_fee=5, initial_balance=0) -> None:
        super().__init__(initial_balance)
        self.withdrawal_fee = withdrawal_fee
    
    # def __repr__(self) -> str:
    #     return f'A HighInterest with ${self.balance:.2f} in it.'
    
    def withdraw(self, value):
        total = self.withdrawal_fee + value
        super().withdraw(total)

class LockedIn(HighInterest):
    """Like a HighInterest sacing account but earning higher interest, without abilty to withdraw demand"""

    interest_rate = .009
    
    def withdraw(self, value):
        return f"Can't make early withdrawal from a Locked-in Saving account."