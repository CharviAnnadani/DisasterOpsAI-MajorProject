def calculate_priority(disaster_type, description):

    disaster_type = disaster_type.lower()
    description = description.lower()

    if disaster_type == "earthquake":
        priority = 5

    elif disaster_type == "flood":
        priority = 4

    elif disaster_type == "fire":
        priority = 4

    else:
        priority = 2

    if (
        "trapped" in description
        or "injured" in description
        or "collapsed" in description
        or "critical" in description
    ):
        priority = 5

    return priority


def assign_rescue_team(disaster_type):

    disaster_type = disaster_type.lower()

    if disaster_type == "earthquake":
        return "Earthquake Response Team"

    elif disaster_type == "flood":
        return "Flood Rescue Team"

    elif disaster_type == "fire":
        return "Fire Emergency Team"

    return "Search and Rescue Team"


def ai_decision(priority):

    if priority == 5:
        return "AI detected critical emergency. Immediate response required."

    elif priority == 4:
        return "AI detected high risk situation. Rescue team assigned."

    elif priority == 3:
        return "AI detected moderate risk. Monitoring recommended."

    return "AI detected low risk emergency."