from tkinter import *
from plyer import notification

def notify():
    notification.notify(
        title=title_entry.get(),
        message=message_entry.get(),
        timeout=10
    )

root = Tk()
root.title("Desktop Notifier")
root.geometry("400x300")

Label(root, text="Notification Title").pack(pady=5)
title_entry = Entry(root, width=40)
title_entry.pack()

Label(root, text="Notification Message").pack(pady=5)
message_entry = Entry(root, width=40)
message_entry.pack()

Button(root, text="Send Notification", command=notify).pack(pady=20)

root.mainloop()