#!/usr/bin/env python3


# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the List of parameters.
# You may introduce private/protected utility methods though.
class Calendar:

    def __init__(self):

        self.events = {}
        self.next_event_id = 1

    def add_event(self, date_str, start_time, end_time, description):
        
        if start_time >= end_time:
            raise Exception(f"The Starttime:{start_time} is bigger or equal to Endtime:{end_time}")
        
        # Create event_id and increase counter by 1
        event_id = self.next_event_id
        self.next_event_id += 1

        # Check if date is already in events
        if date_str not in self.events:
            # Create list for a new date
            self.events[date_str] = []
        
        # Create Entry
        self.events[date_str].append((event_id, start_time, end_time, description))
        return event_id

    def get_events(self, date_str):

        # Check if event exists
        if date_str not in self.events:
            return []
        
        return sorted(self.events[date_str], key=lambda date:date[1])
        
    def delete_event(self, event_id):
        
        # Go through all the events
        for date_str, events in self.events.items():
            for event in events:
                if event[0] == event_id:
                    events.remove(event)
                    return event
        
        raise Exception(f"The Event with if id:{event_id} does not exist")


# You can play around with your implementation in the following body.
# The contained statements will be ignored while evaluating your solution.
if __name__ == "__main__":
    cal = Calendar()
    event_id_dinner = cal.add_event("2024-12-24", "18:00", "20:00", "Christmas Dinner with Family")
    event_id_sleep = cal.add_event("2024-12-24", "21:00", "23:59", "Sleep")
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_dinner)
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_sleep)
    print(cal.get_events("2024-12-24"))
