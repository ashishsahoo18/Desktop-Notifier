from plyer import notification
import time

TITLE = "Study Reminder"
MESSAGE = "Take a short break and drink water."
TIME_INTERVAL = 1800  # 30 minutes

while True:
    notification.notify(
        title=TITLE,
        message=MESSAGE,
        timeout=10
    )

    print("Notification sent")
    time.sleep(TIME_INTERVAL)