def extract_intent(user_input):
    user_input = user_input.lower()

    if "delay" in user_input:
        return "CHECK_DELAY"
    elif "progress" in user_input or "status" in user_input:
        return "CHECK_PROGRESS"
    elif "risk" in user_input:
        return "CHECK_RISK"
    elif "recommend" in user_input or "suggest" in user_input:
        return "RECOMMEND"
    else:
        return "UNKNOWN"
