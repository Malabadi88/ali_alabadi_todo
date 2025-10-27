def test_should_not_send_reminder_if_overdue():
    task = {
        "title": "Submit report",
        "due_time": datetime.now() - timedelta(minutes=10)
    }
    assert should_send_reminder(task) == False
