from support_classes import Timer, DBManager
from RewardService import RewardService
from models.Challenge import Challenge
from screens.Notification import NotificationScreen
from screens.DailyChallenge import DailyChallengeScreen
import main_menu

class ChallengeService:
    def __init__(self, db:DBManager, reward_service:RewardService):
        self.db = db
        self.reward_service = reward_service
        self.current_challenge = None
        self.current_timer = None
        self.current_screen = None

    # when the user clicks "daily challenge" from the main menu this should run
    def start_daily_challenge(self):
        
        try:
            if self.is_daily_completed():
                raise ValueError("Daily challenged has been completed for today")

            challenge = self.create_challenge()
            calories = challenge.get_calories()
            timer = self.create_timer()
            timer.StartTimer()

            dScreen = DailyChallengeScreen()
            dScreen.show()

        except Exception as e:
            error_message = f":{str(e)}"
            nScreen = NotificationScreen(error_message)
            nScreen.show()


    # when the user clicks "Done" in the DailyChallengeScreen
    def challenge_completed(self) -> None:
        self.reward_service.reward_points_to_user(100)
        self.db.save_challenge(self.current_challenge)
        self.current_challenge = None

        nScreen = NotificationScreen("Congrats for completing the daily challenge 100 points have been awarded!")
        nScreen.show()

    # when the user clicks "Abort" in the DailyChallengeScreen
    def challenge_aborted(self) ->None:
        menu = main_menu.MainMenuScreen()
        menu.show()

        nScreen = NotificationScreen("Challenge has been aborted")
        nScreen.show()


    def is_daily_completed(self) -> bool:
        return self.db.is_daily_challenge_completed()

    def create_challenge(self) -> Challenge:
        self.current_challenge = Challenge()
        return self.current_challenge
    
    def create_timer(self) -> Timer:
        self.current_timer = Timer()
        return self.current_timer
    
    def start_timer(self, timer):
        timer.start_timer()
