
from abc import ABC, abstractmethod
import pickle
import time

class AmountLargeError(Exception):
    pass

class ReturnError(Exception):
    pass


class Loans(ABC):
    def create_new_file(self):
        l2=[]
        D2={}
        # file=open("new_one2.pickle","rb")
        
        # l2=pickle.load(file)

        
        self.name=input("enter your name:")
        self.accountno=int(input("enter your account number:"))
        self.cnic_no=int(input("enter your CNIC number:"))
        self.phone=int(input("enter your phone number:"))
        self.guaranter=input("enter the guaranter name:")
        self.salary=int(input("enter your salary:"))
        self.age=int(input("enter your age:"))
        D2["name"]=self.name
        D2["account no"]=self.accountno
        D2["cnic"]=self.cnic_no
        D2["phone_no"]=self.phone
        D2["guaranter"]=self.guaranter
        D2["salary"]=self.salary
        D2["age"]=self.age
        l2.append(D2)
        
        file=open("new_one2.pickle","wb")
        pickle.dump(l2,file)

        
    @abstractmethod
    def abstract(self):
        pass




class Business_loans(Loans):
    def input(self):
        super().create_new_file()

    def abstract(self):

        self.loan=int(input("enter the loan required:"))
        loan=self.salary*10
        returnwithin=2024
        
        try:
            if self.loan > loan:
                raise AmountLargeError
                
        except:
            time.sleep(2.4)
            print("sorry,but you can't take this big amount depending on your salary!")

        else:            
            self.returnit=int(input("you would be returning it within(enter the year):"))
            try:
                if self.returnit > returnwithin:
                    raise ReturnError
            except:
                time.sleep(2.4)
                print("you must return it within the year 2024!")

            else:
                time.sleep(2.4)
                print("Your loan of Rs",self.loan,"has been granted!")
                
        



class House_loans(Loans):
    def input(self):
        super().create_new_file()

    def abstract(self):
        self.category=input("enter your category [house/apartment]")
        self.size=int(input("enter the size in yards"))
        if self.size>2000:
            print("it should be within 2000 yards!")
        else:
            self.location=input("enter the location")
            self.loan=int(input("enter the loan required:"))
            loan=self.salary*10
            returnwithin=2024
        
            try:
                if self.loan > loan:
                    raise AmountLargeError
                
            except:
                time.sleep(2.4)
                print("sorry,but you can't take this big amount depending on your salary!")
            
            else:
                time.sleep(2.4)
                print("Your loan of Rs",self.loan,"has been granted!")


class Car_loans(Loans):
    def input(self):
        super().create_new_file()

    def abstract(self):
        interest=0.01020
        self.name=input("which car would you buy:")
        self.model=int(input("enter its model(year):"))
        self.tenure=int(input("enter the loan tenure(in years):"))
        if self.tenure>5:
            print("should be within 5 years")
        else:
            months=self.tenure*12
            self.loan=int(input("enter the loan required:"))
            if self.loan>1000000:
                print("loan shouldn't increase 10 lacs")
            else:
                EMI=(self.loan*interest*(1+interest)**months)//(((1+interest)**months)-1)
                time.sleep(2.4)
                print("your monthly installments would be Rs",EMI)



