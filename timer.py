import time
from pymsgbox import alert

def display_alert():
    alert("Augen für 20 Sekunden entspannen", "Alert")

while True:
    display_alert()
    time.sleep(1200)  # Sleep for 20 minutes (20 minutes * 60 seconds = 1200 seconds)
