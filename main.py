import time
from datetime import datetime
from plyer import notification 
timeinterval = 60*30
def ScreenBreak():
    notification.notify( app_name = "Screen Break Notifier" , title = "Screen Break", message="It's time to take a sreen break." , timeout=10 ) 
def showCurrentTime():
	current_time = datetime.now().strftime("%H:%M:%S")
	return current_time
print(f"Started program at : {showCurrentTime()} ")	
if __name__ == "__main__":
    while True:
        time.sleep(timeinterval)
        ScreenBreak()
        print(f"Last notified : {showCurrentTime()}")
