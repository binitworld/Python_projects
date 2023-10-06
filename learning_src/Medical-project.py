import random

def get_health_advice():
    """Gets a random health advice."""
    advices = [
        "Eat a healthy diet.",
        "Exercise regularly.",
        "Get enough sleep.",
        "Manage stress.",
        "See your doctor regularly.",]
    return random.choice(advices)

def main():
    """Gets and prints a random health advice."""
    advice = get_health_advice()
    print(advice)

if __name__ == "__main__":
    main()
