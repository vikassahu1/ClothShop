import pywhatkit
from datetime import datetime, timedelta

# Variables
phone_number = '+917021872240'  # Include country code
group_id = '' 
message = 'Write the message here'
waiting_time_to_send = 15  # Time to wait after opening WhatsApp Web
close_tab = True
waiting_time_to_close = 2  # Time to wait before closing the tab

# Get the current time
now = datetime.now()

# Set the time to send the message 1 minute from now
send_time = now + timedelta(minutes=1)
time_hour = send_time.hour
time_minute = send_time.minute

mode = "contact"

try:
    if mode == "contact":
        # Send a WhatsApp message to a specific contact
        pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute, wait_time=waiting_time_to_send, tab_close=close_tab, close_time=waiting_time_to_close)
        print(f"Message scheduled to be sent to {phone_number} at {time_hour}:{time_minute}")
    elif mode == "group":
        # Send a WhatsApp message to a specific group
        pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, wait_time=waiting_time_to_send, tab_close=close_tab, close_time=waiting_time_to_close)
        print(f"Message scheduled to be sent to group {group_id} at {time_hour}:{time_minute}")
    else:
        print("Error code: 97654")
        print("Error Message: Please select a mode to send your message.")
except Exception as e:
    print(f"An error occurred: {e}")
