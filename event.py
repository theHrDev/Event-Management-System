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
        return "Event not registered"
    
   
    if name in events[event]:
        return "name already exist"
    
    
    events[event].append(name)
    return "name added successfully"


def unregistered_user(event,name):
    # global events
    if event not in events:
        return "Event not registered"
    
    if name not in events[event]:
        return "name not registered"
    
    events[event].remove(name)
    return "name removed successfully"

print(unregistered_user("Tech Summit","Taye"))