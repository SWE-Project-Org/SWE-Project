DROP TABLE IF EXISTS DailyCalorieHistory;
DROP TABLE IF EXISTS Challenge;
DROP TABLE IF EXISTS RecentlyScannedFood;
DROP TABLE IF EXISTS ActivityType;
DROP TABLE IF EXISTS Activity;
DROP TABLE IF EXISTS IngredientAllergies;
DROP TABLE IF EXISTS Allergy;
DROP TABLE IF EXISTS Ingredient;
DROP TABLE IF EXISTS FoodIngredient;
DROP TABLE IF EXISTS Food;
DROP TABLE IF EXISTS CouponCodes;
DROP TABLE IF EXISTS User;

CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    daily_calories INTEGER,
    points INTEGER,
    daily_limit INTEGER

);

CREATE TABLE IF NOT EXISTS CouponCodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    calories_per_100g INTEGER NOT NULL,
    carbs REAL,
    proteins REAL,
    fats REAL,
    vitamins REAL
);

CREATE TABLE IF NOT EXISTS FoodIngredient (
    food_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    PRIMARY KEY (food_id, ingredient_id),
    FOREIGN KEY (food_id) REFERENCES Food (id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient (id)
);

CREATE TABLE IF NOT EXISTS Ingredient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calories INTEGER NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Allergy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS  IngredientAllergies (
    ingredient_id INTEGER NOT NULL,
    allergy_id INTEGER NOT NULL,
    PRIMARY KEY (ingredient_id, allergy_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient (id),
    FOREIGN KEY (allergy_id) REFERENCES Allergy (id)
);

CREATE TABLE IF NOT EXISTS Activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_time INTEGER NOT NULL,
    total_calories INTEGER NOT NULL,
    avg_heartrate INTEGER,
    activity_date DATE
);

CREATE TABLE IF NOT EXISTS ActivityType (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    calories_burned_per_hr INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS RecentlyScannedFood (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calories_per_100g INTEGER NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Challenge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    completed BOOLEAN NOT NULL,
    date_of_challenge DATE,
    difficulty TEXT CHECK( difficulty in ('Easy', 'Medium', 'Hard'))
);

CREATE TABLE IF NOT EXISTS DailyCalorieHistory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    calories INTEGER NOT NULL
);
------------------------------------------------------------------

INSERT INTO User (daily_calories, points, daily_limit) 
VALUES (2000, 100, 2500);

/* return ActivityType */
SELECT name,calories_burned_per_hr 
FROM ActivityType;

/* store Activity */
INSERT INTO Activity (total_time, total_calories, avg_heartrate, activity_date) 
VALUES (30, 300, 140, DATE('now'));

/* removed activitycompleted, added date to activity */

/* Update daily_calories */
SELECT daily_calories FROM User;
UPDATE USER SET daily_calories = 200;
/* 200 is a placeholder, value will be passed as a 
 * parameter in the code */

/* Trigger to reset every 24h ενδεικτικα αυτο θα γινει σε python*/
INSERT INTO Challenge (completed, date_of_challenge, difficulty) VALUES (FALSE, DATE('now'), 'Medium');
/* fix: new challenge entry should be created every 24 hrs */

/* Για την επαληθευση του proc if completed = 1 */
SELECT completed FROM Challenge WHERE date_of_challenge = DATE('now');
/* should get only todays challenge, regardless of id*/

/* save challenge mark as completed */
UPDATE Challenge SET completed = TRUE
WHERE date_of_challenge = DATE('now');
/* same as above change todays challenge*/

/* Get RecentlyScannedFood */
SELECT name, calories_per_100g FROM RecentlyScannedFood
ORDER BY id DESC
LIMIT 3;

/* Get Food Info */
SELECT name, calories_per_100g, carbs, proteins, fats, vitamins  FROM Food WHERE name = 'Banana';

/* add some nutrients fields such as vitamins, proteins etc pls */
INSERT INTO Food (name, calories_per_100g, carbs, proteins, fats, vitamins)
VALUES ('Banana', 89, 22.8, 1.1, 0.3,0.2),
       ('Apple', 52, 14, 0.3, 0.2,0.3),
       ('Chicken', 239, 0, 27, 14,0.4),
       ('Rice', 130, 28.7, 2.7, 0.3,0.1);

/* Get Allergies */
SELECT a.name FROM Allergy a
JOIN IngredientAllergies ia ON a.id = ia.allergy_id
JOIN FoodIngredient fi ON ia.ingredient_id = fi.ingredient_id
JOIN Food f ON fi.food_id = f.id
WHERE f.name = 'Banana';

/* Get Ingredients */
SELECT i.name FROM Ingredient i
JOIN FoodIngredient fi ON i.id = fi.ingredient_id
JOIN Food f ON fi.food_id = f.id
WHERE f.name = 'Banana';

/* Save RecentlyScannedFood */
INSERT INTO RecentlyScannedFood (name, calories_per_100g)
VALUES ('Apple', 102);

/* Store Ingredient */
INSERT INTO Ingredient (name, calories) VALUES ('Tomato', 18);


/* Store Food σαν εξτρα αν ειναι περιττο δεν το βαζουμε */
INSERT INTO Food (name, calories_per_100g, carbs, proteins, fats, vitamins)
VALUES ('Banana', 89, 22.8, 1.1, 0.3,0.2),
       ('Apple', 52, 14, 0.3, 0.2,0.3),
       ('Chicken', 239, 0, 27, 14,0.4),
       ('Rice', 130, 28.7, 2.7, 0.3,0.1);

/* Link Food with Ingredients */
INSERT INTO FoodIngredient (food_id, ingredient_id)
VALUES (1, 1);  -- 1 is the id of 'Tomato'

/* Get User points */
SELECT points FROM User LIMIT 1;

/* UPDATE User points */
UPDATE User SET points = 200 WHERE id = 1;

/* insert coupon code */
INSERT INTO CouponCodes (code) VALUES ('SAVE10');

/*get all coupon codes */
SELECT code FROM CouponCodes;

/* get daily calories, limit for "trigger" */
SELECT daily_calories, daily_limit FROM User WHERE id = 1;

/* insert recently scanned */
INSERT INTO RecentlyScannedFood (calories_per_100g, name) 
VALUES (230, 'Chicken');

/* get daily history and activity calories */
SELECT calories FROM DailyCalorieHistory
WHERE date BETWEEN DATE('now', '-7 days') AND DATE('now');
SELECT total_calories FROM Activity
WHERE activity_date BETWEEN DATE('now', '-7 days') AND DATE('now');

/* daily calories reset every 24 hrs and the old value get saved */
INSERT INTO DailyCalorieHistory (date, calories)
VALUES (DATE('now', '-1 days'), (SELECT daily_calories FROM User));

UPDATE User SET daily_calories = 0;