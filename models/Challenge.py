import datetime
import random


class Challenge:
    def __init__(self, calories=0, duration=0, difficulty="Medium", description="", date_of_challenge=None, completed=False):
        self.calories = calories
        self.duration = duration  # minutes
        self.difficulty = difficulty
        self.description = description
        self.date_of_challenge = date_of_challenge
        self.completed = completed

    def get_calories(self) -> int:
        return self.calories

    def create_challenge(self) -> "Challenge":
         challenge = random.choice(challenges)
         self.calories = challenge.calories
         self.duration = challenge.duration
         self.difficulty = challenge.difficulty
         self.description = challenge.description
         self.date_of_challenge = datetime.datetime.now().strftime("%Y-%m-%d")
         return self

    @classmethod
    def from_row(cls, row):
        return cls(
            calories=row[4],
            duration=row[5],
            difficulty=row[3],
            description=row[6],
            date_of_challenge=row[2],
            completed=bool(row[1])
        )

    def to_tuple(self):
        return (self.completed, self.date_of_challenge, self.difficulty, self.calories, self.duration, self.description)

# Random list of challenges
challenges = [
    Challenge(calories=100, duration=10, difficulty="Easy", description="Walk 10 minutes"),
    Challenge(calories=200, duration=15, difficulty="Medium", description="Run 10 minutes"),
    Challenge(calories=300, duration=20, difficulty="Medium", description="Cycle 10 minutes"),
    Challenge(calories=400, duration=25, difficulty="Medium", description="Swim 10 minutes"),
    Challenge(calories=500, duration=30, difficulty="Medium", description="Hike 10 minutes"),
]

