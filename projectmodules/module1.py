
import pickle
import time

class ContactError(Exception):
    pass

class DominationError(Exception):
    pass



class PrizebondNumbers():
    
  

    def new1(self):   
        self.name=input("enter your name")
        try:
            self.prize_bond=int(input("enter prize bond number"))
            self.contact=int(input("enter contact number"))
            if len(str(self.contact))!=11:
                raise ContactError
            

        except ValueError:
            time.sleep(2.4)
            print("please give valid input")

            

        except ContactError:
            time.sleep(2.4) 
            print("contact number should be of 11 digits!")
            
    def new2(self):
        l2=[]
        D2={}
        # file=open("new_one3.pickle","rb")
        # l2=pickle.load(file)

        D2["name"]=self.name
        D2["prize bond number"]=self.prize_bond
        D2["contact number"]=str(self.contact)
        l2.append(D2)
        
        file=open("new_one3.pickle","wb")
        pickle.dump(l2,file)
        file.close()
        time.sleep(2.4)
        print("your information has been saved!")
class PrizebondAward():
    
                
    def awards(self,obj11):
        self.object=obj11
        self.object.new1()
        
        file=open("new_one3.pickle","rb")
        l2=pickle.load(file)

        bondfound=False
        try:
            for award in l2:
                if (award["prize bond number"]==obj11.prize_bond):
                    bondfound=True
                    domination=int(input("enter the denomination[100/200/750/1500/15000/25000]"))
                    if domination==100:
                        category=input("enter the category [1st_prize,2nd_prize,3rd_prize]")
                        if category=="1st_prize":
                            time.sleep(2.4) 
                            print("Your award money is 700000")
                            
                        elif category=="2nd_prize":
                            time.sleep(2.4)
                            print("your award money is 200000")
                        elif category=="3rd_prize":
                            time.sleep(2.4)
                            print("youR award money is 1000")
                        else:
                            raise ValueError
                        
                            
                    
            
                             
                    elif domination==200:
                                            
                        category=input("enter the category [1st_prize,2nd_prize,3rd_prize]")
                        if category=="1st_prize":
                            time.sleep(2.4)
                            print("Your award money is 750000")
                        elif category=="2nd_prize":
                            time.sleep(2.4)
                            print("your award money is 250000")
                        elif category=="3rd_prize":
                            time.sleep(2.4)
                            print("youR award money is 1250")
                        else:
                            raise ValueError
                    elif domination==750:
                                            
                        category=input("enter the category [1st_prize,2nd_prize,3rd_prize]")
                        if category=="1st_prize":
                            time.sleep(2.4)
                            print("Your award money is 1500000")
                        elif category=="2nd_prize":
                            time.sleep(2.4)
                            print("your award money is 500000")
                        elif category=="3rd_prize":
                            time.sleep(2.4)
                            print("youR award money is 9300")
                        else:
                            raise ValueError
                                           
                    elif domination==1500:
                                            
                        category=input("enter the category [1st_prize,2nd_prize,3rd_prize]")
                        if category=="1st_prize":
                            time.sleep(2.4)
                            print("Your award money is 300000 ")
                            
                            
                        elif category=="2nd_prize":
                            time.sleep(2.4)
                            print("your award money is 100000")
                        elif category=="3rd_prize":
                            time.sleep(2.4)
                            print("youR award money is 18500")
                        else:
                            raise ValueError
                    elif domination==7500:
                                            
                         category=input("enter the category [1st_prize,2nd_prize,3rd_prize]")
                         if category=="1st_prize":
                            time.sleep(2.4)
                            print("Your award money is 15000000")
                         elif category=="2nd_prize":
                            time.sleep(2.4) 
                            print("your award money is 5000000")
                         elif category=="3rd_prize":
                            time.sleep(2.4)
                            
                            print("youR award money is 93000")

                         else:
                            raise ValueError
                                           
                    elif domination==15000:
                                            
                        category=input("enter the category [1st_prize,2nd_prize,3rd_prize]")
                        if category=="1st_prize":
                            time.sleep(2.4)
                            print("Your award money is 30000000")
                        elif category=="2nd_prize":
                            time.sleep(2.4)
                            print("your award money is 10000000")
                        elif category=="3rd_prize":
                            time.sleep(2.4)
                            print("youR award money is 185000")

                        else:
                            raise ValueError
                    elif domination==25000:
                                            
                        category=input("enter the category [1st_prize,2nd_prize,3rd_prize]")
                        if category=="1st_prize":
                            time.sleep(2.4)
                            print("Your award money is 50000000")
                        elif category=="2nd_prize":
                            time.sleep(2.4) 
                            print("your award money is 15000000")
                        elif category=="3rd_prize":
                            time.sleep(2.4)
                            print("youR award money is 312000")

                        else:
                            raise ValueError
                    else:
                        raise DominationError
                else:
                    continue                               

        except DominationError as error1:
            time.sleep(2.4)
            print("print enter correct domination")

        except ValueError:
            time.sleep(2.4)
            print("Please choose from the given categories!")

        if bondfound==False:
            time.sleep(2.4)
            print("sorry your bond number does not match")
        
    
    
