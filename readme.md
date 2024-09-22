**README**
---


**Disclaimer**

This script is for educational purposes only and should not be used for actual security systems. It is a demonstration of TkInter's capabilities and not intended to provide secure authentication or access control.

For the alarm sound, the code uses the ***winsound*** library, to get the code working on other OS, all code using this library has to be removed.

The code does not have any other dependencies.


**Script Overview**
---
This script is a TkInter-based GUI application that simulates a passcode-protected door system. It demonstrates various features of TkInter, including:

**Passcode Input**:
A numerical keypad allows users to enter a passcode.

**Authentication**:
The entered passcode is checked against a predefined code. If correct, the door is "unlocked."

**Alarm System**:
If the passcode is incorrect, an alarm sounds, and the system blocks further input for a short period.

**Doorbell**:
A doorbell button triggers a notification and allows the user to grant or deny access.

**Control Panel**:
A separate control window provides buttons to block or unblock the terminal, trigger an alarm, and shut down the system.

**Clock Display**:
A digital clock displays the current time.

**How it Works**
---
The script initializes a TkInter GUI with a passcode input screen, keypad, and doorbell button.

The user enters a passcode using the keypad, and the script checks it against the predefined code.

If the passcode is correct, the door is "unlocked," and a success message is displayed.

If the passcode is incorrect, an alarm sounds, and the system blocks further input for 30 seconds.

The doorbell button triggers a notification, allowing the user to grant or deny access.

The control panel provides additional functionality, such as blocking or unblocking the terminal, triggering an alarm, and shutting down the system.

The digital clock displays the current time.

**Note:**
This script is for educational purposes only and should not be used in production environments or for actual security systems. It is intended to demonstrate TkInter's capabilities and provide a starting point for learning GUI programming in Python.