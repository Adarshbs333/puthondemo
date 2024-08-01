class InsufficientAmount(Exception):
    pass

class wallet(object):
    def __init__(selfinitial_amount=0):
        self.bal=selfinitial_amount
    def spend_cash(self,amount):
        if(self.bal<amount):
            raise InsufficientAmount(f"not enough {amount} to spend")
        self.bal-=amount
    def add_cash(self,amount):
        self.bal+=amount