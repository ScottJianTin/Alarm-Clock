from tkinter import *
import datetime
import time
import winsound

# Define a function that makes the program automatic to work


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Current Time is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake Up...")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

# Define a function that takes in user input for setting the alarm in string format


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


# Initialize tkinter


clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text="Enter time in 24 hour format!",
                    fg="red", bg="black", font="Arial").place(x=60, y=120)
add_time = Label(clock, text="Hour   Min    Sec", font=60).place(x=110)
set_your_alarm = Label(clock, text="When to wake you up?", fg="blue",
                       relief="solid", font=("Helevetica", 7, "bold")).place(x=0, y=29)

# Variables to set the alarm


hour = StringVar()
min = StringVar()
sec = StringVar()

# Time required to set the alarm


hourTime = Entry(clock, textvariable=hour, bg="pink",
                 width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable=min, bg="pink",
                width=15).place(x=150, y=30)
secTime = Entry(clock, textvariable=sec, bg="pink",
                width=15).place(x=200, y=30)

# Submit time input


submit = Button(clock, text="Set Alarm", fg="red", width=10,
                command=actual_time).place(x=110, y=70)

clock.mainloop()
