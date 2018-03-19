import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS account(AccountName TEXT, Password INT, Money REAL, LastTransaction TEXT)")

def data_entry(tpl):
    c.execute("INSERT INTO account VALUES (?, ?, ?, ?)", tpl)
    c.execute("SELECT * FROM account")

def finish():
    c.close()
    conn.commit()
    conn.close

class Account():
    
    def __init__(self, first_name, last_name, password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.money = 0
        self.account_name = first_name + "_" + last_name
        self.parameters = (self.account_name, password, 0, 'none')
        data_entry(self.parameters)

    def deposite(self,amount):

        self.money += amount
        t = (self.money, "deposited " + str(amount), self.account_name)
        c.execute("UPDATE account SET Money = ?, LastTransaction = ? WHERE AccountName = ?", t)

    def withdraw(self, amount):

        if amount <= self.money:
            self.money -= amount
            t = (self.money,"withdrawn " + str(amount), self.account_name)
            c.execute("UPDATE account SET Money = ?, LastTransaction = ? WHERE AccountName = ?", t)

        else:
            print("You don't have that much money")

myAccount = Account("Antonio","Medeiros", 123456)

myAccount.deposite(44.50)

finish()