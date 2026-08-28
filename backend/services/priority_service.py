def calculate_priority(disaster_type):

    if disaster_type.lower() == "earthquake":
        return 5

    elif disaster_type.lower() == "flood":
        return 4

    elif disaster_type.lower() == "fire":
        return 3

    return 1