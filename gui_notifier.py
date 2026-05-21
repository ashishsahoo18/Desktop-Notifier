from tkinter import *
from tkinter import messagebox
from plyer import notification
import threading
import time


def start_notification():
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

    def notify_loop():
        while True:
            notification.notify(
                title=title,
                message=message,
                timeout=10
            )

            print("Notification Sent")
            time.sleep(interval)

    thread = threading.Thread(target=notify_loop)
    thread.daemon = True
    thread.start()

    messagebox.showinfo("Started", "Notification service started")


# Main Window
root = Tk()
root.title("Desktop Notifier App")
root.geometry("400x350")
root.resizable(False, False)

# Heading
heading = Label(
    root,
    text="Desktop Notifier",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

# Title
Label(root, text="Notification Title").pack()
title_entry = Entry(root, width=40)
title_entry.pack(pady=5)

# Message
Label(root, text="Notification Message").pack()
message_entry = Entry(root, width=40)
message_entry.pack(pady=5)

# Time Interval
Label(root, text="Time Interval (seconds)").pack()
time_entry = Entry(root, width=40)
time_entry.pack(pady=5)

# Button
start_btn = Button(
    root,
    text="Start Notification",
    command=start_notification,
    width=25,
    height=2
)
start_btn.pack(pady=20)

# Footer
footer = Label(
    root,
    text="Made with Python",
    font=("Arial", 10)
)
footer.pack(side=BOTTOM, pady=10)

root.mainloop()