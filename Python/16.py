# Krijimi i klasës BankAccount
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        """
        Konstruktori i klasës që inicializon emrin e pronarit të llogarisë dhe bilancin fillestar.
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Metoda për të depozituar një shumë në llogari.
        """
        if amount > 0:
            self.balance += amount
            print(f"Depozituar {amount} në llogarinë e {self.account_holder}.")
        else:
            print("Shuma për depozitë duhet të jetë pozitive.")

    def withdraw(self, amount):
        """
        Metoda për të tërhequr një shumë nga llogaria.
        """
        if amount > self.balance:
            print("Gabim: Fondet nuk janë të mjaftueshme për të bërë tërheqjen.")
        elif amount > 0:
            self.balance -= amount
            print(f"Tërhequr {amount} nga llogaria e {self.account_holder}.")
        else:
            print("Shuma për tërheqje duhet të jetë pozitive.")

    def display_balance(self):
        """
        Metoda për të shfaqur bilancin aktual të llogarisë.
        """
        print(f"Bilanci i llogarisë së {self.account_holder} është {self.balance}.")

# Krijimi i nënklasës SavingsAccount që trashëgon nga BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0.0, interest_rate=0.05):
        """
        Konstruktori i nënklasës që gjithashtu inicializon interesin.
        """
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """
        Metoda për të aplikuar interesin në bilanc.
        """
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interesi i aplikuar është {interest}. Bilanci i ri është {self.balance}.")

# Testimi i klasës BankAccount dhe SavingsAccount
def main():
    # Krijo një instancë të BankAccount
    account1 = BankAccount("Ardit", 1000)
    account1.display_balance()
    
    # Depozito para
    account1.deposit(500)
    account1.display_balance()

    # Tërheq para
    account1.withdraw(300)
    account1.display_balance()

    # Provoni të tërheqni më shumë se bilanci
    account1.withdraw(2000)
    
    # Krijo një instancë të SavingsAccount
    savings_account = SavingsAccount("Klea", 2000, 0.03)
    savings_account.display_balance()
    
    # Depozito para
    savings_account.deposit(1000)
    savings_account.display_balance()

    # Apliko interesin
    savings_account.apply_interest()
    savings_account.display_balance()

# Ekzekuto funksionin main për të testuar
if __name__ == "__main__":
    main()
