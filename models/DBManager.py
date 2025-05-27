from models.Challenge import Challenge
import sqlite3
import datetime

from models.CouponCode import CouponCode

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.insert_activity_type()
        self.insert_user()

    def is_daily_challenge_completed(self) -> bool:
        # Get today's date in YYYY-MM-DD format
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute('''
            SELECT * FROM Challenge 
            WHERE date_of_challenge = ? AND completed = 1
        ''', (today,))
        row = self.cursor.fetchone()
        return row is not None

    def save_challenge(self, challenge: Challenge) -> None:
        self.cursor.execute('''
            INSERT INTO Challenge 
            (completed, date_of_challenge, difficulty, calories, duration, description)
            VALUES (?, ?, ?, ?, ?, ?);
        ''', challenge.to_tuple())
        self.conn.commit()

    def get_user_points(self) -> int:
        self.cursor.execute('SELECT points FROM User LIMIT 1;')
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]
        return 0

    # returns balance
    def subtract_user_points(self, amount: int) -> int:
        user_points = self.get_user_points()
        new_points = user_points - amount
        self.update_user_points(new_points)
        return new_points

    def update_user_points(self, points: int) -> None:
        self.cursor.execute('UPDATE User SET points = ? WHERE id = 1;', (points,))
        self.conn.commit()

    def reward_points_to_user(self, points: int) -> None:
        current_points = self.get_user_points()
        new_points = current_points + points
        self.update_user_points(new_points)

    # save the coupon code
    def save_coupon_code(self, coupon_code) -> None:
        self.cursor.execute(
            'INSERT INTO CouponCodes (code, description, validTill) VALUES (?, ?, ?);',
            (coupon_code.code, coupon_code.description, coupon_code.validTill.strftime('%Y-%m-%d'))
        )
        self.conn.commit()

    def get_all_coupon_codes(self):
        self.cursor.execute('SELECT code, description, validTill FROM CouponCodes;')
        return self.cursor.fetchall()

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
            VALUES (0, 2000, ?);
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
        self.cursor.execute('DROP TABLE IF EXISTS Challenge;')
        self.cursor.execute('DROP TABLE IF EXISTS CouponCodes;')
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
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Challenge (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                completed BOOLEAN NOT NULL,
                date_of_challenge DATE,
                difficulty TEXT CHECK( difficulty in ('Easy', 'Medium', 'Hard')),
                calories INT,
                duration INT,
                description TEXT
            );
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CouponCodes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL,
                description TEXT,
                validTill DATE
            );
        ''')
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
        return self.get_consumed_calories() - self.get_burned_calories()
    
    def get_daily_limit(self):
        self.cursor.execute('SELECT daily_limit FROM User;')
        return self.cursor.fetchone()[0]
    
    def get_burned_calories(self):
        self.cursor.execute('SELECT SUM(total_calories) FROM Activity;')
        return self.cursor.fetchone()[0] or 0
    
    def get_consumed_calories(self):
        self.cursor.execute('SELECT SUM(calories) FROM RegisteredFood;')
        return self.cursor.fetchone()[0] or 0
    
    def store_food(self, calories):
        self.cursor.execute('''
            INSERT INTO RegisteredFood (calories)
            VALUES (?);
        ''', (calories,))
        self.conn.commit()
        
        