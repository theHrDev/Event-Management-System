class User:
    def __init__(self,name):
        self.name = name

class Event:
    def __init__(self,event):
        self.event = event
        

class Events:
    def __init__(self,id,event,users):
        self.id = id
        self.event = event
        self.users = users
        
    def register_user(self,u):
        pass