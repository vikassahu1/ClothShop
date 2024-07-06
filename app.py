import os
import json
import sys
from datetime import datetime
# from dataclasses import dataclass
from utils import log_value,get_net_profit,day_wise_log,read_transactions_by_date
from exceptions import CustomException


class Transaction:
    def __init__(self, left_pant, left_tshirt, pant_sale, tshirt_sale, total_money,pant_loss, tshirt_loss, salary, other_exp, today, note,profit,pre_lost,paytm,cash_money):
        self.left_pant = left_pant
        self.left_tshirt = left_tshirt
        self.pant_sale = pant_sale
        self.tshirt_sale = tshirt_sale
        self.total_money = total_money
        self.pant_loss = pant_loss
        self.tshirt_loss = tshirt_loss
        self.salary = salary
        self.other_exp = other_exp
        self.today = today
        self.note = note
        self.profit = profit
        self.lost = pre_lost
        self.paytm = paytm
        self.cash_money= cash_money

    def prepare_msg(self):
        msg = f"Transaction Details:\n"
        msg += f"Date: {self.today}\n\n"
        msg += f"Left Pant: {self.left_pant}\n"
        msg += f"Left Tshirt: {self.left_tshirt}\n"
        msg += f"Pant Sale: {self.pant_sale}\n"
        msg += f"Tshirt Sale: {self.tshirt_sale}\n"
        
        msg += f"Pant Loss: {self.pant_loss}\n"
        msg += f"Tshirt Loss: {self.tshirt_loss}\n\n"

        msg += f"Total Money: {self.total_money}\n"
        msg += f"Salary: {self.salary}\n"
        msg += f"Other Expenses: {self.other_exp}\n"
        msg += f"Note: {self.note}\n\n"

        msg += f"Profit: {self.profit}\n"
        msg += f"Money-Lost: {self.lost}\n"
        msg += f"Paytm: {self.paytm}\n"
        msg += f"Cash in Hand: {self.cash_money}\n"

        
        print(f"\n{msg}Transaction Completed!\n")
        return msg


    def alldata(self):
        msg = self.prepare_msg()
        log_value(msg,self.today)
        day_wise_log(self.today,self.cash_money,self.paytm,self.salary,self.profit,self.lost,self.note)
        # send_whatsapp_message("Hisab",msg)
        print("All logs completed !")

 

class Update_Material:
    def __init__(self):
        self.file_path = 'materials.json'
        with open(self.file_path) as f:
            data = json.load(f)
        self.pant = data['pant']
        self.tshirt = data['tshirt']

    def getPant(self):
        return self.pant

    def getTshirt(self):
        return self.tshirt

    def update_pant(self, new_pant):
        self.pant = new_pant
        self.save()

    def update_tshirt(self, new_tshirt):
        self.tshirt = new_tshirt
        self.save()

    def save(self):
        data = {'pant': self.pant, 'tshirt': self.tshirt}
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def update_function(self):
        no_of_pants_added = int(input("Enter number of new pants added: "))
        no_of_tshirts_added = int(input("Enter number of new tshirts added: "))
        self.update_pant(pant+no_of_pants_added)
        self.update_tshirt(tshirt+no_of_tshirts_added)

    

if __name__ == "__main__":
    try: 
        print("1.Log Value\n2.Update Material\n3.See Data\n4.Lost Material",end="\n\n")
        num = int(input("Enter the Choice: "))

        # To get material (tshirt and pants)
        materials = Update_Material()
        pant = materials.getPant()
        tshirt = materials.getTshirt()

        if(num==1):
            # Handling Updates if any 
            update = input("Is there any Update (y/n): ")
            if(update=='y'):
                materials.update_function()
                pant = materials.getPant()
                tshirt = materials.getTshirt()
            else:
                pass


            # Taking pant and tshirt values from json file 
            left_pant  = int(input("Pants Left: "))
            left_tshirt = int(input("Tshirts Left: "))
            pant_sale = pant - left_pant
            tshirt_sale = tshirt - left_tshirt

            total_money = (pant_sale * 150) + (tshirt_sale *200)
            

            print("Total Money: ",total_money,end="\n")
            pant_loss = int(input("Pant Loss: "))
            tshirt_loss =  int(input("Tshirt Loss: "))

            # Calculating profit and loss
            pre_profit,pre_lost = get_net_profit(total_money,pant_sale,tshirt_sale,pant_loss,tshirt_loss)
            print("Prliminary-Profit: ",pre_profit)
            print("Preliminary-Money Lost: ",pre_lost)

            # pants and tshirts left after adjusting all losses 
            pant = left_pant-pant_loss
            tshirt = left_tshirt - tshirt_loss

            # Updating materials to new value 
            materials.update_pant(pant)
            materials.update_tshirt(tshirt)
            
            salary = int(input("Enter Salesman Salary: "))
            other_exp = int(input("Enter Other Expenditure: "))

            # Calculating all type of money.
            paytm = int(input("Money in Paytm: "))
            cash_money = total_money - (pre_lost + paytm + salary  + other_exp)
            profit = pre_profit-salary-other_exp

            print(f"Cash in hand should be: {cash_money}")
            print("Profit left: ",profit)
 
            # Note: Lost money is not considered in ultimate profit of the day to save it separate 
            today = input("Enter date of storing (yyyy-mm-dd): ")
            note = input("Enter Note if any: \n")



            # Storing, Printing and Sending msg 
            # pre_lost is money_lost  
            representing = Transaction(left_pant,left_tshirt,pant_sale,tshirt_sale,total_money,pant_loss,tshirt_loss,salary,other_exp,today,note,profit,pre_lost,paytm,cash_money)
            representing.alldata()
            

        elif(num==2):
            materials.update_function()
            pant = materials.getPant()
            tshirt = materials.getTshirt()

        elif(num==3):
            date = input("Enter date in yyyy-mm-dd format: ")
            read_transactions_by_date(date)

    except Exception as e:
        raise CustomException(e,sys)



        

        