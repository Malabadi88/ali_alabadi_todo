from datetime import datetime, timedelta

def should_send_reminder(task):
    one_hour = timedelta(hours=1)
    time_until_due = task["due_time"] - datetime.now()
    return timedelta(0) < time_until_due <= one_hour
