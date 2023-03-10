import win32evtlog
import win32api
import win32security
import datetime

events_list = []

def grab_event_logs(log_type):
    global events_list
    try: 
        hand = win32evtlog.OpenEventLog(None, log_type)# event handler to grab logs by log type from localhost
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ #logs are called newest to oldest

        while True: #needs while loop to get all logs 
            events = win32evtlog.ReadEventLog(hand, flags, 0)#returns list of events
            for event in events:
                events_list.append(event)
            if not events:
                break

        win32evtlog.CloseEventLog(hand) 
    except BaseException:
        print("Run VS Code as admin")


#Start of program
def main_menu():
    print("Welcome! Which log type would you like to look at? \nEnter num for selection.")
    print("1 - System \n2 - Security \n3 - Application \n")
    user_in = int(input("Enter number: "))
    if(user_in == 1):
        grab_event_logs("System")
    elif(user_in == 2):
        grab_event_logs("Security")
    elif(user_in == 3):
        grab_event_logs("Application")
    else:
        print("invalid input. Try again.")
        main_menu()

main_menu()
print(len(events_list))