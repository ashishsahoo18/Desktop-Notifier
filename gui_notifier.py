from tkinter import *
from tkinter import messagebox
from plyer import notification
import winsound
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

        # Sound Play
        winsound.MessageBeep()

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

# Background Color
root.configure(bg="#1e1e2f")

# Heading
Label(
    root,
    text="Desktop Notifier",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
).pack(pady=10)

# Title
Label(
    root,
    text="Notification Title",
    bg="#1e1e2f",
    fg="white"
).pack()

title_entry = Entry(
    root,
    width=40,
    bg="#2d2d44",
    fg="white",
    insertbackground="white"
)
title_entry.pack(pady=5)

# Message
Label(
    root,
    text="Notification Message",
    bg="#1e1e2f",
    fg="white"
).pack()

message_entry = Entry(
    root,
    width=40,
    bg="#2d2d44",
    fg="white",
    insertbackground="white"
)
message_entry.pack(pady=5)

# Time
Label(
    root,
    text="Time Interval (seconds)",
    bg="#1e1e2f",
    fg="white"
).pack()

time_entry = Entry(
    root,
    width=40,
    bg="#2d2d44",
    fg="white",
    insertbackground="white"
)
time_entry.pack(pady=5)

# Start Button
Button(
    root,
    text="Start Notification",
    command=start_notification,
    width=25,
    height=2,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049"
).pack(pady=10)

# Stop Button
Button(
    root,
    text="Stop Notification",
    command=stop_notification,
    width=25,
    height=2,
    bg="#f44336",
    fg="white",
    activebackground="#d32f2f"
).pack(pady=5)

root.mainloop()