import os
from datetime import datetime, timedelta
import pywhatkit as pwk


def getDate():
    pass

def calculate_loss():
    pass


def send_whatsapp_message(group_name, message):
    # Get current time
    now = datetime.now()

    # Adjust time parameters for immediate sending (1 second delay)
    send_time = now + timedelta(seconds=1)
    hours = send_time.hour
    minutes = send_time.minute

    # Send message to group
    pwk.sendwhatmsg_to_group(group_name, message, hours, minutes, wait_time=10)





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