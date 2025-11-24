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
    "Sports Festival": ["Lilly","Killy"],
    "Music Fiesta": ["Poppoal","koll","kktl"]
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
    for names in events:
        return names


def event_management(menu):
    if menu == "1":
        event = input("Enter the event name: ")
        name = input("Enter user's name: ")
        register_user(event=event,name=name)
    elif menu == "2":
        event = input("Enter the event name: ")
        name = input("Enter user's name: ")
        unregistered_user(event,name)
    elif menu == "3":
        event = input("Enter the event name: ")
        get_participants(event)
    else:
        exit()

menu = input("Choose a menu: \n 1. Register user \n 2. Unregister user \n 3. View participants \n 4. Show event with fewest participants \n 5. Show event with most participants \n 6. Exit: ")
event_management(menu=menu)
    






        

# print(unregistered_user("Tech Summit","Taye"))