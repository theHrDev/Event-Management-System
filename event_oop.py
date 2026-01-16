import random
class User:
    def __init__(self,name):
        self.name = name

class Event:
    def __init__(self,id,event):
        self.id = id
        self.event = event
        self.users = []
        

        
        

class Events:
    def __init__(self):
        self.events = {}
        
    def generate_id(self):
        random_id = random.randint(10*5,10*6-1)  

        event_id = f"event{random_id}"
        if event_id not in self.events:
            return event_id; 
    
    def create_event(self,event_name):
        event_id = self.generate_id()
        new_event = Event(id=event_id,event=event_name)
        self.events[event_id] = new_event
        return f"event created successfully"  
          
    def edit_event(self,event_id,event_name):
        if event_id not in self.events:
            return "invalid id"
        self.events[event_id].event = event_name
        return "event edited successfully"
    
    def view_event(self,event_id):
        if not event_id in self.events:
            return "invalid event id"
        match_event = self.events[event_id]
        return f"id: {match_event.id} \n event: {match_event.event} users: {match_event.users} "
    
    def view_all_events(self):
        if not self.events:
            return "no event found"
        results = []
        for e in self.events.values():
            results.append(f"id:{e.id} event : {e.event}  users: {e.users}")
        return "\n".join(results)
    
    def delete_event(self,event_id):
        if not event_id in self.events:
            return "invalid event id"
        del self.events[event_id]
        return "Event deleted successfully"
    
class Enroller:
    def __init__(self,events,user):
            self.events =  events
            self.user = user
            
    def register_user(self,event_id):
            if not event_id in self.events.events:
                return "invalid id"
            
            self.events.events[event_id].users.append(self.user)
            return "User enroll successfully"
            
        
    def unregister_user(self,event_id):
            pass
        
    def get_participant(self,event_id):
            pass
        
    
def event_menu(menu):
    print('Welcome, Pick one out of the menu below')
    print('-------- 1. Add Event ---------------')
    print('-------- 2. Remove Event ---------------')
    print('-------- 3. Edit Event ---------------')
    print('-------- 4. Delete Event ---------------')

    
    