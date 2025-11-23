# 11. Event Registration Manager

# Use a dictionary:

# events = {
#   "Tech Summit": [],
#   "Sports Festival": [],
#   "Music Fiesta": []
# }


# Functions:

# register_user(event, name)

# unregister_user(event, name)

# get_participants(event)

# find_events_with_lowest_participants()

# find_events_with_highest_participants()


events = {
    "Tech Summit":["Taye", "Kenny"],
    "Sports Festival": [],
    "Music Fiesta": []
}

# print(events["Tech Summit"][0])


def register_user(event,name):
    # global events
    if event not in events:
        return f"{event} event not registered"
    
   
    if name in events[event]:
        return f"{name} already exist"
    
    
    events[event].append(name)
    return f"{name} registered successfully for {event} event"


def unregistered_user(event,name):
    # global events
    if event not in events:
        return f"{event} event not registered"
    
    if name not in events[event]:
        return f"{name} not registered"
    
    events[event].remove(name)
    return f"{name} removed successfully"

def get_participants(event):
    if event not in events:
        return f"{event} event not registered"
    
    return events[event]

def find_events_with_lowest_participants():
    min = 0
    for event in events:
        total_num = len(event)
        if min > total_num:
            min = total_num
            
    return f"The event with the lowest num is {event}"
        






        

# print(unregistered_user("Tech Summit","Taye"))