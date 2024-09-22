from tkinter import *
from tkinter import font
import time
import random
from datetime import datetime
import winsound

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

print(CGREEN2 + "Startup..." + CEND)
tryinput = []
tries = 0
block = False
rung = False
accept_input = True


code = [0,0,0,0,0,0,0,0,0,0]
codeaccepted = False

shutdown_request = False

while codeaccepted == False:
    codein = input(CYELLOW2 + "Please enter numeric code to start: " + CEND)
    try:
        codeval = int(codein)
        codeaccepted = True
        code = [int(digit) for digit in str(codeval)]  # Add this line
        print(CGREENBG2 + "System startup..." + CEND)
        break
    except ValueError:
        print(CREDBG + "Wrong Format - Code has to be numeric!" + CEND)
        continue

def panic():
    alarm()
    block_terminal()

def on_closing_control_window():
    displayWindow.destroy()

def create_control_window():
    global controlWindow
    controlWindow = Tk()
    controlWindow.title("Control window")
    controlWindow.geometry("400x250")
    controlWindow.configure(bg="#b3b3b3")
    controlWindow.resizable(False, False)


    cwFrame1 = Frame(controlWindow, width=800, height=60, bg='red')
    cwFrame1.place(x=0, y=0, relx=0.00, rely=0.00)
    Label(cwFrame1, font=("TkDefaultFont", 10), text="Control Panel", relief=RAISED, height=3, width=50, justify=CENTER).grid(row=0, column=0, padx=0, pady=0)
    
    cwFrame2 = Frame(controlWindow, width=800, height=60, bg='red')
    cwFrame2.place(x=0, y=70, relx=0.00, rely=0.00)
    
    Button(cwFrame2, text="Block Terminal", command=block_terminal, relief=RAISED, height=3, width=15, justify=CENTER).grid(row=0, column=0, padx=0, pady=0)
    Button(cwFrame2, text="Alarm", command=alarm, relief=RAISED, height=3, width=15, justify=CENTER, bg="yellow").grid(row=0, column=1, padx=0, pady=0)
    Button(cwFrame2, font=("TkDefaultFont"), text="PANIC", command=panic, relief=RAISED, height=3, width=24, justify=CENTER, bg="red", fg="white").grid(row=0, column=2, padx=0, pady=0)

    cwFrame3 = Frame(controlWindow, width=800, height=60, bg='red')
    cwFrame3.place(x=0, y=150, relx=0.00, rely=0.00)

    Button(cwFrame3, text="Disable Terminal", command=disable_terminal, relief=RAISED, height=3, width=15, justify=CENTER).grid(row=0, column=1, padx=0, pady=0)
    Button(cwFrame3, text="Enable Terminal", command=enable_terminal, relief=RAISED, height=3, width=15, justify=CENTER).grid(row=0, column=2, padx=0, pady=0)
    Button(cwFrame3, font=("TkDefaultFont"), text="Shutdown", command=shutdown_terminal, relief=RAISED, height=3, width=24, justify=CENTER, bg="blue", fg="white").grid(row=0, column=3, padx=0, pady=0)

    controlWindow.mainloop()

def disable_terminal():
    global block, tryinput, accept_input
    accept_input = False
    tryinput = []
    print(CGREENBG2 + "Terminal disabled..." + CEND)
    block = True
    display_screen.config(text="Terminal is disabled.", fg="red")
    display_screen.config(state="disabled")

def enable_terminal():
    global block
    global accept_input
    accept_input = True
    print(CGREENBG2 + "Terminal enabled..." + CEND)
    block = False
    display_screen.config(state="normal")
    return_to_standard()

def shutdown_terminal():
    global shutdown_request
    if shutdown_request == False:
        shutdown_request = True
        should_shutdown = input("Shutdown? (Y|N) ")
        if should_shutdown == "Y":
            displayWindow.destroy()
            controlWindow.destroy()
        else:
            shutdown_request = False

def unlock():
    print(CYELLOWBG + CBLACK + "Door has been unlocked!" + CEND)
    display_screen.after(3, print(CBLUEBG + CWHITE + "Door has been locked." + CEND))

def ring_bell():
    global rung, tryinput
    if accept_input == True:
        if rung == False:
            rung = True
            tryinput = []
            # Modern doorbell sound (a series of short, high-pitched beeps)
            for i in range(2):
                winsound.Beep(2800, 500)  # 2800 Hz frequency, 100 ms duration
                time.sleep(0.05)  # 50 ms pause between beeps
            print(CYELLOWBG + CBLACK + "Doorbell has been pressed!" + CEND)
            display_screen.config(text="Notification sent, please wait...", fg="#e6b800")
            db_accept = input(CVIOLET + CWHITE + "OPEN? (Y|N)" + CEND)
            if db_accept == "Y":
                display_screen.config(text="Unlocked!", fg="green")
                unlock()
            else:
                print(CGREENBG + CWHITE + "Declined!" + CEND)
                display_screen.config(text="Request denied.", fg="red")
        
            displayWindow.after(3000, return_to_standard)  # return to standard after 1 seconds
            rung = False



def one_in():
    global accept_input
    if accept_input == True:
        tryinput.append(1)
        reload_display()

def two_in():
    global accept_input
    if accept_input == True:
        tryinput.append(2)
        reload_display()

def three_in():
    global accept_input
    if accept_input == True:
        tryinput.append(3)
        reload_display()

def four_in():
    global accept_input
    if accept_input == True:
        tryinput.append(4)
        reload_display()

def five_in():
    global accept_input
    if accept_input == True:
        tryinput.append(5)
        reload_display()

def six_in():
    global accept_input
    if accept_input == True:
        tryinput.append(6)
        reload_display()

def seven_in():
    global accept_input
    if accept_input == True:
        tryinput.append(7)
        reload_display()

def eight_in():
    global accept_input
    if accept_input == True:
        tryinput.append(8)
        reload_display()

def nine_in():
    global accept_input
    if accept_input == True:
        tryinput.append(9)
        reload_display()

def zero_in():
    global accept_input
    if accept_input == True:
        tryinput.append(0)
        reload_display()

def del_in():
    global accept_input
    if accept_input == True:
        if tryinput != []:
            tryinput.pop()
            reload_display()

def reload_display():
    display_screen.config(text=tryinput)
    reload_time()

def reload_time():
    now = datetime.now()
    clocktime.config(text=now.strftime("%H:%M:%S"))
    clocktime.after(1000, reload_time)  # update clock every 1 second

failed_attempts = 0


def check_input():
    if accept_input == True:
        global tries, failed_attempts, block, tryinput  # Add tryinput to the global variables
        if block == False:
            if tries < 9:
                if len(tryinput) != 0:
                    if tryinput == code:
                        print(CREDBG + CBLACK + "Unlocked at " + clocktime.cget("text") + CEND)
                        display_screen.config(text="Unlocked!", fg="green")
                        unlock()
                        display_screen.after(3000, return_to_standard)
                        tryinput = []
                    else:
                        print(CREDBG + CBLACK + "WARNING - Wrong Input at " + clocktime.cget("text") + CEND)
                        display_screen.config(text="Incorrect, please try again!", fg="red")
                        display_screen.after(500, return_to_standard)
                        tries += 1
                        failed_attempts += 1
                        if failed_attempts >= 5:  # block input after 5 failed attempts
                            block = True
                            display_screen.config(text="Too many tries, please try again later.", fg="red")
                            displayWindow.after(30000, unblock)  # unblock input after 30 seconds
                            tryinput = []
            else:
                display_screen.config(text="Too many tries, please try again later.", fg="red")
                displayWindow.after(10000, return_to_standard)  # return to standard after 10 seconds
                failed_attempts = 0
                tries = 0
                tryinput = []
        else:
            display_screen.config(text="Door system is blocked.", fg="red")
            alarm()
            tryinput = []

def unblock():
    global block
    block = False
    return_to_standard()


def alarm():
    print(CREDBG + CBLACK + "ALARM - Door system emergency block at " + clocktime.cget("text") + " - Alert security!" + CEND)
    for i in range(5):
        print(CREDBG + CBLACK + "ALARM - Alert security!" + CEND)
        time.sleep(1)
        print(CYELLOWBG + CBLACK + "ALARM - Alert security!" + CEND)
        winsound.Beep(2500, 1000)  # 2500 Hz frequency, 1000 ms duration


def return_to_standard():
    display_screen.config(text="Please enter passcode and press [OK]", fg="black")

def block_terminal():
    global block
    block = True


print(CGREENBG + "Display started!" + CEND)

displayWindow = Tk()
displayWindow.title("Passcode Input")
displayWindow.geometry("855x600")
displayWindow.configure(bg="#b3b3b3")
displayWindow.resizable(True,True)

frame1 = Frame(displayWindow, width=800, height=60, bg='red')
frame1.place(x=0, y=25, relx=0.00, rely=0.00)

display_screen = Label(frame1, font=("Verdana", 20), text="Please enter passcode and press [OK]", relief=RAISED, height=3, width=50, justify=CENTER)
display_screen.grid(row=0, column=0, padx=0, pady=0)

frame2 = Frame(displayWindow, width= 600, height=100, bg='red')
frame2.place(x=0, y=150, relx=0.00, rely=0.00)

Button(frame2, font=("Verdana", 11), text="7", relief=RAISED, height=3, width=23, justify=CENTER, command=seven_in).grid(row=0, column=1, padx=0, pady=0)
Button(frame2, font=("Verdana", 11), text="8", relief=RAISED, height=3, width=23, justify=CENTER, command=eight_in).grid(row=0, column=2, padx=0, pady=0)
Button(frame2, font=("Verdana", 11), text="9", relief=RAISED, height=3, width=23, justify=CENTER, command=nine_in).grid(row=0, column=3, padx=0, pady=0)

frame3 = Frame(displayWindow, width= 600, height=100, bg='red')
frame3.place(x=0, y=260, relx=0.00, rely=0.00)

Button(frame3, font=("Verdana", 11), text="4", relief=RAISED, height=3, width=23, justify=CENTER, command=four_in).grid(row=0, column=1, padx=0, pady=0)
Button(frame3, font=("Verdana", 11), text="5", relief=RAISED, height=3, width=23, justify=CENTER, command=five_in).grid(row=0, column=2, padx=0, pady=0)
Button(frame3, font=("Verdana", 11), text="6", relief=RAISED, height=3, width=23, justify=CENTER, command=six_in).grid(row=0, column=3, padx=0, pady=0)

frame4 = Frame(displayWindow, width= 600, height=100, bg='red')
frame4.place(x=0, y=370, relx=0.00, rely=0.00)

Button(frame4, font=("Verdana", 11), text="1", relief=RAISED, height=3, width=23, justify=CENTER, command=one_in).grid(row=0, column=1, padx=0, pady=0)
Button(frame4, font=("Verdana", 11), text="2", relief=RAISED, height=3, width=23, justify=CENTER, command=two_in).grid(row=0, column=2, padx=0, pady=0)
Button(frame4, font=("Verdana", 11), text="3", relief=RAISED, height=3, width=23, justify=CENTER, command=three_in).grid(row=0, column=3, padx=0, pady=0)

frame5 = Frame(displayWindow, width= 600, height=100, bg='red')
frame5.place(x=0, y=480, relx=0.00, rely=0.00)

Button(frame5, font=("Verdana", 11), text="0", relief=RAISED, height=3, width=23, justify=CENTER, command=zero_in).grid(row=0, column=1, padx=0, pady=0)
Button(frame5, font=("Verdana", 11), text="DEL", background="red", foreground="white", relief=RAISED, height=3, width=23, justify=CENTER, command=del_in).grid(row=0, column=2, padx=0, pady=0)
Button(frame5, font=("Verdana", 11), text="OK", background="green",foreground="white", relief=RAISED, height=3, width=23, justify=CENTER, command=check_input).grid(row=0, column=3, padx=0, pady=0)
Button(frame5, font=("Verdana", 12), text="🔔", background="#ffff66",foreground="black", relief=RAISED, height=3, width=20, justify=CENTER, command=ring_bell).grid(row=0, column=4, padx=0, pady=0)

frame6 = Frame(displayWindow, width= 100, height=300, bg='red')
frame6.place(x=675, y=150, relx=0.00, rely=0.00)

clocktime = Label(frame6, font=("Verdana", 18), text="00:00", relief=RAISED, height=2, width=10, justify=CENTER)
clocktime.grid(row=0, column=0, padx=0, pady=0)

reload_time()
create_control_window()

displayWindow.mainloop()
