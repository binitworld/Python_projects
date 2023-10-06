from prettytable import PrettyTable

def create_timetable():
    # Create a timetable
    timetable = PrettyTable()
    
    # Add columns to the timetable
    timetable.field_names = ["Time", "Activity"]
    
    # Add rows to the timetable
    timetable.add_row(["06:00 AM", "Wake up"])
    timetable.add_row(["06:30 AM", "Brush"])
    timetable.add_row(["07:00 AM", "study"])
    timetable.add_row(["09:00 AM", "Work"])
    timetable.add_row(["12:30 PM", "Lunch"])
    timetable.add_row(["01:30 PM", "work"])
    timetable.add_row(["05:00 PM", "Snack"])
    timetable.add_row(["06:00 PM", "break"])
    timetable.add_row(["07:30 PM", "gym"])
    timetable.add_row(["09:00 PM", "Dinner"])
    timetable.add_row(["09:30 PM", "Relaxation"])
    timetable.add_row(["10:00 PM", "Study"])
    timetable.add_row(["12:30 PM", "Bed Time"])
    
    # Print the timetable
    print(timetable)

# Call the function to create and display the timetable
create_timetable() 