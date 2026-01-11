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
          
    def edit_event(self):
        pass
    def view_event(self):
        pass
    def delete_event(self):
        pass