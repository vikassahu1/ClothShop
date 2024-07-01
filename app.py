import os
import json
from datetime import datetime
from dataclasses import dataclass
from utils import calculate_loss,getDate

# pant = 300
# tshirt = 300
# cash,gpay


class EnterValue:
    def __init__(self):
        pass


    def enter(self):
        pass



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
    



if __name__ == "__main__":
    print("1.Log Value\n2.Update Material\n3.See Data\n4.Lost Material",end="\n\n")
    num = int(input("Enter the Choice: "))

    # To get material (tshirt and pants)
    materials = Update_Material()
    pant = materials.getPant()
    tshirt = materials.getTshirt()

    print(pant)


    if(num==1):
        update = int(input("Is there any Update (y/n): "))
        if(update=='y'):
            no_of_pants_added = int(input("Enter number of new pants added: "))
            no_of_tshirts_added = int(input("Enter number of new tshirts added: "))
            materials.update_pant(pant+no_of_pants_added)
            materials.update_tshirt(tshirt+no_of_tshirts_added)
            pant = materials.getPant()
            tshirt = materials.getTshirt()
        
        # Taking pant and tshirt values from json file 

        left_pant  = int(input("Pants Left: "))
        left_tshirt = int(input("Tshirts Left: "))
        pant_sale = pant - left_pant
        tshirt_sale = tshirt - left_tshirt

        total_money = (pant_sale * 150) + (tshirt_sale *200)

        print("Total Money: ",total_money,end="\n")
        pant_loss = int(input("Pant Loss: "))
        tshirt_loss =  int(input("Tshirt  Loss: "))

        pant = left_pant-pant_loss
        tshirt = left_tshirt - tshirt_loss
        
        salary = int(input("Enter Salesman Salary: "))
        other_exp = int(input("Enter Other Expenditure: "))

        # Storing the values int txt,json and initiating whattsapp msg


    elif(num==2):
        pass


        

        







        

