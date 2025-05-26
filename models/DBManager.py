from models.Challenge import Challenge
import sqlite3


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.insert_activity_type()
        self.insert_user()

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

    def insert_user(self, daily_limit=2000):
        self.cursor.execute('''
            INSERT INTO User (daily_calories, points, daily_limit)
            VALUES (0, 0, ?);
        ''', (daily_limit,))
        self.conn.commit()
    
    def get_activities(self):
        self.cursor.execute('SELECT * FROM ActivityType;')
        return self.cursor.fetchall()

    def create_tables(self):
        self.cursor.execute('DROP TABLE IF EXISTS ActivityType;')
        self.cursor.execute('DROP TABLE IF EXISTS Activity;')
        self.cursor.execute('DROP TABLE IF EXISTS User;')
        self.cursor.execute('DROP TABLE IF EXISTS RegisteredFood;')
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
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            daily_calories INTEGER,
            points INTEGER,
            daily_limit INTEGER
        );''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS RegisteredFood (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            calories INTEGER
        );''')

        self.conn.commit()

    def store_activity(self, 
                       total_time, 
                       total_calories, 
                       avg_heartrate):
        self.cursor.execute('''
            INSERT INTO Activity (total_time, total_calories, avg_heartrate, activity_date)
            VALUES (?, ?, ?, DATE('now'));
        ''', (total_time, total_calories, avg_heartrate))
        self.conn.commit()

    def update_calorie_counter(self):
        burned_calories = self.get_consumed_calories()
        consumed_calories = self.get_burned_calories()
        self.cursor.execute('''
            UPDATE User
            SET daily_calories = daily_calories - ?;
        ''', ((consumed_calories - burned_calories),))
        self.conn.commit()

    def get_calorie_counter(self):
        self.cursor.execute('SELECT daily_calories FROM User;')
        return self.cursor.fetchone()[0]
    
    def get_daily_limit(self):
        self.cursor.execute('SELECT daily_limit FROM User;')
        return self.cursor.fetchone()[0]
    
    def get_burned_calories(self):
        self.cursor.execute('SELECT SUM(total_calories) FROM Activity;')
        return self.cursor.fetchone()[0] or 0
    
    def get_consumed_calories(self):
        self.cursor.execute('SELECT SUM(calories) FROM RegisteredFood;')
        return self.cursor.fetchone()[0] or 0
        