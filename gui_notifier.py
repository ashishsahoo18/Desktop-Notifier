from tkinter import *
from tkinter import messagebox
from plyer import notification
import threading
import time

running = False


def notify_loop(title, message, interval):
    global running

    while running:
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )

        print("Notification Sent")
        time.sleep(interval)


def start_notification():
    global running

    title = title_entry.get()
    message = message_entry.get()
    interval = time_entry.get()

    if title == "" or message == "" or interval == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        interval = int(interval)
    except:
        messagebox.showerror("Error", "Time must be a number")
        return

    if not running:
        running = True

        thread = threading.Thread(
            target=notify_loop,
            args=(title, message, interval)
        )

        thread.daemon = True
        thread.start()

        messagebox.showinfo("Started", "Notifications Started")


def stop_notification():
    global running
    running = False
    messagebox.showinfo("Stopped", "Notifications Stopped")


# Window
root = Tk()
root.title("Desktop Notifier")
root.geometry("400x350")
root.resizable(False, False)

Label(
    root,
    text="Desktop Notifier",
    font=("Arial", 18, "bold")
).pack(pady=10)

# Title
Label(root, text="Notification Title").pack()
title_entry = Entry(root, width=40)
title_entry.pack(pady=5)

# Message
Label(root, text="Notification Message").pack()
message_entry = Entry(root, width=40)
message_entry.pack(pady=5)

# Time
Label(root, text="Time Interval (seconds)").pack()
time_entry = Entry(root, width=40)
time_entry.pack(pady=5)

# Start Button
Button(
    root,
    text="Start Notification",
    command=start_notification,
    width=25,
    height=2
).pack(pady=10)

# Stop Button
Button(
    root,
    text="Stop Notification",
    command=stop_notification,
    width=25,
    height=2
).pack(pady=5)

root.mainloop()