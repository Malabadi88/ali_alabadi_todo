from datetime import datetime, timedelta

# For now, define the function here directly
# (Later we’ll import it from reminder.py)
def should_send_reminder(task):
    one_hour = timedelta(hours=1)
    time_until_due = task["due_time"] - datetime.now()
    return timedelta(0) < time_until_due <= one_hour

def test_should_send_reminder_with_upcoming_task():
    task = {"due_time": datetime.now() + timedelta(minutes=30)}
    assert should_send_reminder(task) is True
