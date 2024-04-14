import random
import sample


#The simple bank application will simulate basic banking functionalities such as account creation, balance inquiry, deposit, withdrawal, and transaction history.
import re
class Bank :
    def __init__(self):
        self.Accounts = []
        self.Accounts = sample.data_gen()

    def acc_create(self):
        acc_num = ""
        arr = []
        name = input("Enter Account name : ").upper().replace(" ","")
        password = input("Set password : ")
        for i in range(6):
            anum = str(random.randrange(0, 9))
            arr.append(anum)
            acc_num = " ".join(arr)
        intial_deposit = float(input("Enter a Intial Deposit Ammount : "))
        self.Accounts.append({
            "name" : name,
            "password" : password,
            "acc_num"  : acc_num,
            "intial_deposit" : intial_deposit,
            "transaction" : []
        })
        print("Account Created Successfully !")



    def verify(func):
        def check(self,name1,password1):
            for temp in self.Accounts:
                if name1 == temp['name'] and password1 == temp['password']:
                    return func(self,name1,password1)
            else:
                raise Exception("Invalid credentials!")
        return check

    @verify
    def depo_sit(self,name2,password2):
        print("")
        print("! 3.Deposit: !")
        ammount1 = float(input("Enter amount to Deposit : "))
        for temp in self.Accounts:
            if name2 == temp['name'] and password2 == temp['password']:
                temp['intial_deposit'] += ammount1
                temp['transaction'].append(f"{ammount1} is Credited")
                print("Successfully Done !")

    @verify
    def with_draw(self, name2, password2):
        print("")
        print("! 4.Withdrawal: !")
        ammount1 = float(input("Enter amount to Deposit : "))
        for temp in self.Accounts:
            if name2 == temp['name'] and password2 == temp['password']:
                temp['intial_deposit'] -= ammount1
                temp['transaction'].append(f"{ammount1} is Debited")
                print("Successfully Done !")

    @verify
    def tran_saction(self,name2, password2):
        print("")
        print("! 5.Transaction History: !")
        for i,temp in self.Accounts:
            if name2 == temp['name'] and password2 == temp['password']:
                print(f"`{temp['transaction'][i]}`")
    def acc_info (self,):
        for temp in self.Accounts:
            if not temp:
                print("Thers is no Customers !")
            else:
                print(temp)

    @verify
    def balance(self,name2,password2):
        print("")
        print("! 2.Balance Inquiry: !")
        for temp in self.Accounts:
            if name2 == temp['name'] and password2 == temp['password']:
                return temp['intial_deposit']

    @verify
    def up_date(self, name2, password2):
        print(" 1.Name 2.Password ")
        option3 = int(input("Enter which info as to be update : "))
        for temp in self.Accounts:
            if name2 == temp['name'] and password2 == temp['password']:
                if option3 == 1 :
                    ps1 = input("Enter new Name : ")
                    temp['name'] = ps1
                    print("Done....")
                elif option3 == 2 :
                    us1 = input("Enter new Password : ")
                    temp['password'] = us1
                    print("Done....")
    @verify
    def delete(self,name,password):
        for temp in self.Accounts:
            if name == temp['name'] and password == temp['password']:
                del temp['name'],temp['password'],temp['acc_num'],temp['intial_deposit'],temp['transaction']
                print("Deleted Successfully !")



        

def main():
    cust1 = Bank()
    while True:
        print("")
        print("                      <<<<<<<<<<<<<<< WELCOME TO BANKING APPLICATION >>>>>>>>>>>>>>>")
        print("Select your Operations on Your Account >> ")
        print("1.Account Creation:    | 2.Balance Inquiry:    | 3.Deposit: | 4.Withdrawal: ")
        print("5.Transaction History: | 6.Account Management: | 7.Account Information: | 8 . Exit: ")
        print("")
        option = None
        try:
            option = int(input("Select your Option : "))
        except ValueError as e:
            print(e)
            return main()

        if option == 1:
            print("")
            print("!!Account Creation!!")
            cust1.acc_create()
        elif option == 2:
            name = input("Enter your name : ").upper().replace(" ", "")
            password2 = input("Enter your password : ")
            try:
                balresult = cust1.balance(name, password2)
                print(f"Balance : {balresult}")
            except Exception as e:
                print(e)

        elif option == 3:
            name = input("Enter your name : ").upper().replace(" ", "")
            password2 = input("Enter your password : ")
            try:
                cust1.depo_sit(name, password2)
            except Exception as e:
                print(e)

        elif option == 4:
            name = input("Enter your name : ").upper().replace(" ", "")
            password2 = input("Enter your password : ")
            try:
                cust1.with_draw(name, password2)
            except Exception as e:
                print(e)

        elif option == 5:
            name = input("Enter your name : ").upper().replace(" ", "")
            password2 = input("Enter your password : ")
            try:
                cust1.tran_saction(name, password2)
            except Exception as e:
                print(e)

        elif option == 6:
            print("")
            print("! 6.Account Management: !")
            print("Select to Modify : ")
            print(" 1. Update 2. Delete  ")
            option1 = int(input("Enter the Option : "))
            while True:
                if option1 == 1:
                    name = input("Enter your name : ").upper().replace(" ", "")
                    password2 = input("Enter your password : ")
                    cust1.up_date(name, password2)
                    break
                elif option1 == 2:
                    name = input("Enter your name : ").upper().replace(" ", "")
                    password2 = input("Enter your password : ")
                    cust1.delete(name, password2)
                    break

        elif option == 7:
            print("! 7.Account Information of All Customers !")
            print("")
            cust1.acc_info()

        else:
            exit(0)

                                    #driver code >>>>>>>>>>>
if __name__ == "__main__":
    main()