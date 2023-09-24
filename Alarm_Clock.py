from tkinter import *
import datetime
import time
from playsound import playsound

def set_alarm():
    global alarm_time
    hour_val = int(hour.get())
    if am_pm.get() == "PM":
        hour_val += 12
    alarm_time = datetime.time(hour=hour_val, minute=int(minute.get()))
    label.config(text=f"Alarm set for {alarm_time.strftime('%I:%M %p')}")
    set_button.config(state=DISABLED)  # Disable the set button after alarm is set
    stop_button.pack_forget()  # Hide the stop button
    check_alarm()

def check_alarm():
    current_time = datetime.datetime.now().time()
    if current_time >= alarm_time:
        trigger_alarm()
    else:
        clock.after(1000, check_alarm)  # Check again in 1 second

def trigger_alarm():
    label.config(text=f"Alarm triggered at {alarm_time.strftime('%I:%M %p')}")
    playsound("D:\\mixkit-alarm-tone-996.wav")  # Replace with the path to your sound file
    set_button.config(state=NORMAL)  # Enable the set button
    stop_button.pack(pady=10)  # Show the stop button

def stop_alarm():
    label.config(text="Alarm stopped")
    set_button.config(state=NORMAL)  # Enable the set button
    stop_button.pack_forget()  # Hide the stop button

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("350x250")

frame = Frame(clock, padx=10, pady=10)
frame.pack(pady=10)

Label(frame, text="Set Alarm", font=("Helvetica", 16)).grid(row=0, columnspan=4, pady=(0, 10))

hour = Spinbox(frame, from_=1, to=12, width=3, font=("Helvetica", 12))
hour.grid(row=1, column=0, padx=(0, 5))

Label(frame, text=":", font=("Helvetica", 12)).grid(row=1, column=1)

minute = Spinbox(frame, from_=0, to=59, width=3, font=("Helvetica", 12))
minute.grid(row=1, column=2, padx=(5, 0))

am_pm = StringVar(value="AM")
am_pm_dropdown = OptionMenu(frame, am_pm, "AM", "PM")
am_pm_dropdown.config(font=("Helvetica", 12))
am_pm_dropdown.grid(row=1, column=3, padx=(5, 0))

set_button = Button(frame, text="Set Alarm", font=("Helvetica", 12), command=set_alarm)
set_button.grid(row=2, columnspan=4, pady=(10, 0))

stop_button = Button(clock, text="Stop Alarm", font=("Helvetica", 12), command=stop_alarm)

label = Label(clock, text="", font=("Helvetica", 14))
label.pack(pady=10)

clock.mainloop()
