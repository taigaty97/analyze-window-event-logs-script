import win32evtlog
import win32api
import win32security
import datetime

def check_event_log(event_id):
    event_found = False
    hand = win32evtlog.OpenEventLog(None, "Security")# None refers to 'local', System refers to log type
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(hand, flags, 0)

    for event in events:
        
        print(type(event))
        #print(event.EventID,event.TimeGenerated)
        '''
        if event_id == event.EventID:
            event_found = True
            print("Event Found - Event ID:", event.EventID)
            print("Event Time Generated:", event.TimeGenerated)
            print("Event Source Name:", event.SourceName)
            print("Event String:", event.StringInserts)
            print("\n")
        
    if not event_found:
        print("Event Not Found - Event ID:", event_id)
    '''
check_event_log(105)
