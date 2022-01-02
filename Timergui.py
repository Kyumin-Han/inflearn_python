from tkinter import *
import time

def startTimer():
    if(running):
        global second
        global minute
        global hour
        second += 1
        time.sleep(1)
        secondText.configure(text="%02d" % second)
        minuteText.configure(text="%02d" % minute)
        hourText.configure(text="%02d" % hour)
        if second == 59:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
    window.after(10, startTimer)

def start():
    global running
    running = True

def stop():
    global running
    running = False

def reset():
    global running
    global second
    if not running:
        second = 0
        secondText.configure(text=str(second))

running = False

window = Tk()
window.geometry("640x480+600+250")

second, minute, hour = 58, 59, 0

colonText1 = Label(window, text=":", font=("Helvetica", 80))
colonText2 = Label(window, text=":", font=("Helvetica", 80))

colonText1.grid(row=0, column=1)
colonText2.grid(row=0, column=3)

secondText = Label(window, text="%02d" % second, font=("Helvetica", 60), width=3)
secondText.grid(row=0, column=4)

minuteText = Label(window, text="%02d" % minute, font=("Helvetica", 60), width=3)
minuteText.grid(row=0, column=2)

hourText = Label(window, text="%02d" % hour, font=("Helvetica", 60), width=3)
hourText.grid(row=0, column=0)

def stop1(event):
    global running
    running = False
secondText.bind("<Button-1>", stop1)

def start1(event):
    global running
    running = True
secondText.bind("<Button-1>", start1)

def reset1(event):
    global second
    if not running:
        second = 0
        secondText.configure(text=str(second))
secondText.bind("Button-1", reset1)

startButton = Button(window, text='시작', bg="yellow", command=start)
startButton.grid(row=1, column=0)

stopButton = Button(window, text='중지', bg="yellow", command=stop)
stopButton.grid(row=1, column=1)

resetButton = Button(window, text='초기화', bg="yellow", command=reset)
resetButton.grid(row=1, column=2)



startTimer()
window.mainloop()