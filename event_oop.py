import random

# ---------- MODELS ----------

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Event:
    def __init__(self, id, event):
        self.id = id
        self.event = event
        self.users = []


class Events:
    def __init__(self):
        self.events = {}

    def generate_id(self):
        while True:
            random_id = random.randint(50, 59)
            event_id = f"event{random_id}"
            if event_id not in self.events:
                return event_id

    def create_event(self, event_name):
        event_id = self.generate_id()
        self.events[event_id] = Event(event_id, event_name)
        return f"Event created successfully → {event_id}"

    def edit_event(self, event_id, event_name):
        if event_id not in self.events:
            return "Invalid event id"
        self.events[event_id].event = event_name
        return "Event edited successfully"

    def view_event(self, event_id):
        if event_id not in self.events:
            return "Invalid event id"
        e = self.events[event_id]
        return f"""
ID: {e.id}
Event: {e.event}
Users: {', '.join(map(str, e.users)) or 'No participants'}
"""

    def view_all_events(self):
        if not self.events:
            return "No events found"
        result = []
        for e in self.events.values():
            result.append(
                f"{e.id} | {e.event} | Users: {len(e.users)}"
            )
        return "\n".join(result)

    def delete_event(self, event_id):
        if event_id not in self.events:
            return "Invalid event id"
        del self.events[event_id]
        return "Event deleted successfully"


# ---------- ENROLLMENT ----------

class Enroller:
    def __init__(self, events, user):
        self.events = events
        self.user = user

    def register_user(self, event_id):
        if event_id not in self.events.events:
            return "Invalid event id"

        event = self.events.events[event_id]
        if self.user in event.users:
            return "User already registered"

        event.users.append(self.user)
        return "User enrolled successfully"

    def unregister_user(self, event_id):
        if event_id not in self.events.events:
            return "Invalid event id"

        event = self.events.events[event_id]
        if self.user not in event.users:
            return "User not registered"

        event.users.remove(self.user)
        return "User removed successfully"

    def get_participant(self, event_id):
        if event_id not in self.events.events:
            return "Invalid event id"
        users = self.events.events[event_id].users
        return users if users else "No participants"


# ---------- MENU ----------

def event_menu():
    events = Events()
    user_name = input("Enter your name: ")
    user = User(user_name)
    enroller = Enroller(events, user)

    while True:
        print("\n====== EVENT MENU ======")
        print("1. Add Event")
        print("2. Edit Event")
        print("3. View Event")
        print("4. View All Events")
        print("5. Delete Event")
        print("6. Register for Event")
        print("7. Unregister from Event")
        print("8. View Event Participants")
        print("9. Exit")

        choice = input("Select option: ")

        if choice == "1":
            name = input("Event name: ")
            print(events.create_event(name))

        elif choice == "2":
            eid = input("Event ID: ")
            name = input("New event name: ")
            print(events.edit_event(eid, name))

        elif choice == "3":
            eid = input("Event ID: ")
            print(events.view_event(eid))

        elif choice == "4":
            print(events.view_all_events())

        elif choice == "5":
            eid = input("Event ID: ")
            print(events.delete_event(eid))

        elif choice == "6":
            eid = input("Event ID: ")
            print(enroller.register_user(eid))

        elif choice == "7":
            eid = input("Event ID: ")
            print(enroller.unregister_user(eid))

        elif choice == "8":
            eid = input("Event ID: ")
            print(enroller.get_participant(eid))

        elif choice == "9":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option")


# ---------- RUN ----------
event_menu()
