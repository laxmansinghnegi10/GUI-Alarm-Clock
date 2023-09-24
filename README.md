# GUI-Alarm-Clock-system-using-python
Here's an explanation of the code:

1- Import necessary modules:

* tkinter: Used for creating the GUI.
* datetime: Used for handling time and date.
* time: Used for time-related operations.
* playsound: Used for playing a sound file.


2- Define functions:

* set_alarm(): This function is called when the user clicks the "Set Alarm" button. It sets the alarm time based on the user's input and updates the label to display the alarm time. It also disables the "Set Alarm" button and hides the "Stop Alarm" button.

* check_alarm(): This function checks if the current time has reached the set alarm time. If it has, it calls trigger_alarm(), otherwise, it waits for 1 second and checks again.

* trigger_alarm(): This function is called when the alarm time is reached. It updates the label to indicate that the alarm has been triggered, plays an alarm sound, enables the "Set Alarm" button, and displays the "Stop Alarm" button.

* stop_alarm(): This function is called when the user clicks the "Stop Alarm" button. It updates the label to indicate that the alarm has been stopped, enables the "Set Alarm" button, and hides the "Stop Alarm" button.

3- Create the main window:

* Create a Tk instance named clock.
* Set the title to "Alarm Clock".
* Set the window dimensions to 350x250 pixels.


4- Create a frame:

* Create a Frame named frame within the clock window. This frame will contain the widgets (labels, spinboxes, buttons) for setting the alarm.


5-Add widgets to the frame:

* Add a label "Set Alarm" to the frame.
* Add a spinbox for setting the hour.
* Add a label ":" for separating hours and minutes.
* Add a spinbox for setting the minutes.
* Add a dropdown menu for selecting AM or PM.
* Add a "Set Alarm" button to trigger the alarm.
* Configure the widgets with their respective fonts and positions.

 
6-Create a "Stop Alarm" button and a label for displaying messages.


7- Start the GUI main loop using clock.mainloop().


This code creates a simple alarm clock GUI application where users can set an alarm time and trigger the alarm. When the alarm goes off, it plays a sound. Users can also stop the alarm using the "Stop Alarm" button.







