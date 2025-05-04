class Challenge:
    def __init__(self):
        self.calories = 0
        self.duration = 0 # minutes
        self.difficulty = "Medium"
        self.description = ""

    def get_calories(self) -> int:
        pass

    def create_challenge(self) -> "Challenge":
        # pick a random challenge from a predefined list
        pass