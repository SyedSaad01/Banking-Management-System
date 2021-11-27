
import pickle
import time


class AmountisGreaterError(Exception):
    pass

class AmountisEqualError(Exception):
    pass


class Deposit():
    def deposit(self,account_no):
        file=open("new_one.pickle","rb")
        l=pickle.load(file)
        amount1=int(input("you want to deposit Rs"))
        accountFound=False
        for amount in l:
            if (amount["accountno"]==account_no):
                time.sleep(2.4)
                print("your previous balance was Rs",amount["amount"],"/=")
                amount["amount"]+= amount1
                file=open("new_one.pickle","wb")
                pickle.dump(l,file)
                file.close()
                
                time.sleep(2.4)

                print("your new balance is Rs",amount["amount"],"/=")
                accountFound=True
        if accountFound==False:
            time.sleep(2.4)
            print("account not found")

class Withdraw():
    def withdraw(self,account_no):
        file=open("new_one.pickle","rb")
        l=pickle.load(file)
        amount2=int(input("you want to withdraw Rs"))
        accountFound=False
        for x in l:
            if (x["accountno"]==account_no):
                time.sleep(2.4)
                print("your current balance is Rs",x["amount"])
                try:
                    if (x["amount"] < amount2):
                        raise AmountisGreaterError
                    elif (x["amount"] == amount2):
                        raise AmountisEqualError

                        
                except AmountisGreaterError as error1:
                    time.sleep(2.4)
                    print("sorry,the amount you entered is more than your current balance!")
                    
                except AmountisEqualError as error2:
                    x["amount"]-=amount2
                    file=open("new_one.pickle","wb")
                    pickle.dump(l,file)
                    file.close()
                    
                    time.sleep(2.4)
                    print("your new balance is Rs 0.00")
                    

                else:
                    x["amount"]-=amount2
                    file=open("new_one.pickle","wb")
                    pickle.dump(l,file)
                    file.close()
                    time.sleep(2.4)
                    print("your new balance is Rs",x["amount"])

