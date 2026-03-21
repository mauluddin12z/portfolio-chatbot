def validate_question(q: str):
    q = q.strip()

    if len(q) < 3:
        return False, "Question too short"

    if len(q) > 300:
        return False, "Question too long"

    blocked = ["ignore previous", "system prompt", "jailbreak"]

    for b in blocked:
        if b in q.lower():
            return False, "Invalid question"

    return True, None