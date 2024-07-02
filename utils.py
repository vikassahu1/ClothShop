import os
from datetime import datetime
import pywhatkit as pwk


def getDate():
    pass

def calculate_loss():
    pass


def send_whatsapp_message(phone_number, message):
    now = datetime.now()
    hours = now.hour
    minutes = now.minute + 2  # Send the message 2 minutes from now
    pwk.sendwhatmsg(phone_number, message, hours, minutes)

def log_value(log_data):
    today = datetime.today().strftime('%Y-%m-%d')
    log_file = f"log_{today}.txt"
    with open(log_file, 'a') as f:
        f.write(log_data + '\n')


import os
from datetime import datetime

def log_value(log_data,today):
    # Create a directory named 'logs' if it doesn't exist
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    # Generate log file path based on current date
    # today = datetime.today().strftime('%Y-%m-%d')
    log_file = os.path.join(log_dir, f"log_{today}.txt")

    # Write log_data to the log file
    with open(log_file, 'a') as f:
        f.write(log_data + '\n')