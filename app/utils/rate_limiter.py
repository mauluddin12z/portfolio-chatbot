from datetime import datetime
from collections import defaultdict

user_usage = defaultdict(list)

LIMIT = 10

def is_allowed(user_id: str):
    today = datetime.now().date()

    # filter hanya hari ini
    user_usage[user_id] = [
        t for t in user_usage[user_id]
        if t.date() == today
    ]

    if len(user_usage[user_id]) >= LIMIT:
        return False

    user_usage[user_id].append(datetime.now())
    return True