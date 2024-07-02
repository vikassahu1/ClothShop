import os
import json
import sys
from datetime import datetime
from dataclasses import dataclass
from utils import send_whatsapp_message,log_value,get_net_profit
from exceptions import CustomException


class Transaction:
    def __init__(self, left_pant, left_tshirt, pant_sale, tshirt_sale, total_money,pant_loss, tshirt_loss, salary, other_exp, today, note,profit,net_lost):
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
        self.lost = net_lost

    def prepare_msg(self):
        msg = f"Transaction Details:\n"
        msg += f"Date: {self.today}\n"
        msg += f"Left Pant: {self.left_pant}\n"
        msg += f"Left Tshirt: {self.left_tshirt}\n"
        msg += f"Pant Sale: {self.pant_sale}\n"
        msg += f"Tshirt Sale: {self.tshirt_sale}\n"
        msg += f"Total Money: {self.total_money}\n"
        msg += f"Pant Loss: {self.pant_loss}\n"
        msg += f"Tshirt Loss: {self.tshirt_loss}\n"
        msg += f"Salary: {self.salary}\n"
        msg += f"Other Expenses: {self.other_exp}\n"
        msg += f"Note: {self.note}\n"
        print(f"\n{msg}Transaction Completed!\n")
        return msg


    def alldata(self):
        msg = self.prepare_msg()
        log_value(msg,self.today)
        send_whatsapp_message("Hisab",msg)

 

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
            net_profit,net_lost = get_net_profit(total_money,pant_sale,tshirt_sale,pant_loss,tshirt_loss)
            print(net_profit)
            print(net_lost)

            # pants and tshirts left after adjusting all losses 
            pant = left_pant-pant_loss
            tshirt = left_tshirt - tshirt_loss

            # Updating materials to new value 
            materials.update_pant(pant)
            materials.update_tshirt(tshirt)
            
            salary = int(input("Enter Salesman Salary: "))
            other_exp = int(input("Enter Other Expenditure: "))

            # Storing the values int txt,json and initiating whattsapp msg
            profit = net_profit-salary-other_exp
            print("Profit left: ",profit)
 
            today = input("Enter date of storing (yyyy-mm-dd): ")
            note = input("Enter Note if any: \n")



            # Storing, Printing and Sending msg 
            representing = Transaction(left_pant,left_tshirt,pant_sale,tshirt_sale,total_money,pant_loss,tshirt_loss,salary,other_exp,today,note,profit,net_lost)
            representing.alldata()
            

        elif(num==2):
            materials.update_function()
            pant = materials.getPant()
            tshirt = materials.getTshirt()

        elif(num==3):
            pass

    except Exception as e:
        raise CustomException(e,sys)



        

        







        

