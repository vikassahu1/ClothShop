import os
import json
import csv
from datetime import datetime, timedelta
import pywhatkit as pwk


def send_whatsapp_message(group_name, message):
    # To send transaction details in grp....to be upgraded using selenium 
    #current time
    now = datetime.now()

    # (1 second delay)
    send_time = now + timedelta(seconds=1)
    hours = send_time.hour
    minutes = send_time.minute

    #message to group
    pwk.sendwhatmsg_to_group(group_name, message, hours, minutes, wait_time=10)


def get_cost_price():
    file_name = 'average_cost.json'
    with open(file_name) as f:
            data = json.load(f)
    pant_cp= data['pant_cost_price']
    tshirt_cp = data['tshirt_cost_price']
    return pant_cp,tshirt_cp


def get_net_profit(total_amount,pant_sold,tshirts_sold,pant_loss,tshirt_loss):
    cost_price_pants,cost_price_tshirt = get_cost_price()
    pr = total_amount-((pant_sold*cost_price_pants) + (tshirts_sold*cost_price_tshirt))
    lt = (pant_loss*cost_price_pants) + (tshirt_loss*cost_price_tshirt)
    return pr,lt



def log_value(log_data,today):
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"log_{today}.txt")

    with open(log_file, 'a') as f:
        f.write(log_data + '\n')


def day_wise_log(today,cash_in_hand,money_in_gpay,salary,profit,money_lost,note):
    file_name = 'daywise_info.csv'
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today, cash_in_hand, money_in_gpay, salary, profit, money_lost, note])


def read_transactions_by_date(input_date):
    try:
        with open('transactions.csv', mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  
            transactions = [row for row in reader if row[0] == input_date]
            if transactions:
                print(f"Transactions for {input_date}:")
                for transaction in transactions:
                    print(transaction)
            else:
                print(f"No transactions found for {input_date}.")
    except FileNotFoundError:
        print("No transactions logged yet.")
    except Exception as e:
        print(f"An error occurred: {e}")



def read_transactions_by_date(date):
    with open("daywise_info.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        x=0
        lst = ['Date','Cash in Hand','Money in Paytm','Salary','Profit','Money Lost','Note']
        for row in reader:
            if row[0] == date: 
                for i in range(len(row)):
                    print(f"{lst[i]} : {row[i]}")
                x=1
                break
    if(x==0):
        print("No transactions on given date available")
