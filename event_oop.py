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
        
    def generate_id():
        random_id = random.randint(10*5,10*6-1)   
        event_id = f"event{random_id}"
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
        return f"id: {match_event.id} \n event: {match_event.event} user: {match_event.user} ",
    
    def view_all_events(self):
        if not self.events:
            return "no event found"
        results = []
        for e in self.events:
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
    
    