class Bank:
    bank_name = "default banl"

    def __init__(self , account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls , name):
        cls.bank_name = name

    def display(self):
        print(f"Account holder : {self.account_holder} , bank : {self.bank_name}")


account1 = Bank("ubaid")
account2 = Bank("raza")

account1.display()
account2.display()

Bank.change_bank_name("HBL")


account1.display()
account2.display()
