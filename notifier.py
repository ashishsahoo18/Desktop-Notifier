from plyer import notification
import time

while True:
    notification.notify(
        title="Reminder",
        message="Dark water and take a short break. ",
        timeout=10
    )

    time.sleep(1800)