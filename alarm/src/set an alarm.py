import time
import os

while True:
    # Input the time for the alarm in 24-hour format (e.g., "13:45" for 1:45 PM)
    alarm_time = input("Enter the time for the alarm (HH:MM): ")

    # Split the input into hours and minutes
    hours, minutes = map(int, alarm_time.split(':'))

    # Get the current time
    current_time = time.localtime()
    current_hours = current_time.tm_hour
    current_minutes = current_time.tm_min

    # Calculate the time difference for the alarm
    time_difference = (hours - current_hours) * 3600 + (minutes - current_minutes) * 60

    if time_difference <= 0:
        print("Invalid time. Please set a future time.")
    else:
        print(f"Alarm set for {hours:02d}:{minutes:02d}.")

        # Wait for the specified time
        time.sleep(time_difference)

        # When the alarm time is reached, play a sound (replace 'favsound.mp3' with your alarm sound file)
        alarm_sound = 'favsound.mp3'  # Replace with your sound file path
        os.system(f"start {alarm_sound}")

        print("Time to wake up!")
        break
