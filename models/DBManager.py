from models.Challenge import Challenge
import sqlite3


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.insert_activity_type()
    


    def store_activity(self):
        pass

    def update_calorie_counter(self):
        pass

    def is_daily_challenge_completed(self) -> bool:
        pass

    def save_challenge(self, challenge: Challenge) -> None:
        pass

    def get_user_points(self) -> int:
        pass

    # returns balance
    def subtract_user_points(self) -> int:
        pass

    def update_user_points(self, points: int) -> None:
        pass

    # save the coupon code
    def save_coupon_code(self):
        pass

    def get_all_coupon_codes(self):
        pass

    def get_weekly_data(self):
        return 'weekly data'
    
    def get_recently_scanned_foods(self):
        return 'return_recently_scanned_foods'
    
    def get_info(self):
        return 'info'
    
    def get_ingredients(self):
        return 'ingredients'
    
    def get_allergies(self):
        return 'allergies'
    
    def save_recently_scanned_food(self, recently_scanned_food):
        pass

    def match_image_to_food(self):
        return 'MatchedFood'
    
    def fetch_prices(self):
        return 'prices'
    
    def storeIngredientList(self):
        pass

    def insert_activity_type(self,):
        self.cursor.execute('''
            INSERT INTO ActivityType 
            (name, calories_burned_per_hr)
            VALUES (?, ?);
        ''', ('Running', 600))
        self.cursor.execute('''
            INSERT INTO ActivityType 
            (name, calories_burned_per_hr)
            VALUES (?, ?);
        ''', ('Walking', 300))
        self.conn.commit()
    
    def get_activity_types(self):
        self.cursor.execute('SELECT * FROM ActivityType;')
        return self.cursor.fetchall()

    def create_tables(self):
        self.cursor.execute('DROP TABLE IF EXISTS ActivityType;')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ActivityType (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            calories_burned_per_hr INTEGER NOT NULL
            );''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        total_time INTEGER NOT NULL,
        total_calories INTEGER NOT NULL,
        avg_heartrate INTEGER,
        activity_date DATE
        );''')
        self.conn.commit()