import random


class Challenge:
    def __init__(self, calories=0, duration=0, difficulty="Medium", description=""):
        self.calories = calories
        self.duration = duration  # minutes
        self.difficulty = difficulty
        self.description = description

    def get_calories(self) -> int:
        return self.calories

    def create_challenge(self) -> "Challenge":
        return random.choice(challenges)

# Random list of challenges
challenges = [
    Challenge(calories=100, duration=10, difficulty="Easy", description="Walk 10 minutes"),
    Challenge(calories=200, duration=15, difficulty="Medium", description="Run 10 minutes"),
    Challenge(calories=300, duration=20, difficulty="Medium", description="Cycle 10 minutes"),
    Challenge(calories=400, duration=25, difficulty="Medium", description="Swim 10 minutes"),
    Challenge(calories=500, duration=30, difficulty="Medium", description="Hike 10 minutes"),
]

