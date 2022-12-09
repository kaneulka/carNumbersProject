import sqlite3

con = sqlite3.connect("TestDB") 
cursor = con.cursor()

#Create tables
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        userId INT PRIMARY KEY,
        fname TEXT,
        lname TEXT);
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
        carId INT PRIMARY KEY,
        carNumber TEXT,
        carModel TEXT,
        userId INT,
        FOREIGN KEY (userId) REFERENCES users (userId) ON DELETE CASCADE ON UPDATE CASCADE);
    """)
con.commit()

#Create data
newUsers = [(1, 'Иван', 'Иванов'), 
      (2, 'Ирина', 'Петрова'), 
      (3, 'Екатерина', 'Иванова'), 
      (4, 'Игорь', 'Васильев'), 
      (5, 'Петр', 'Васильев')]
cursor.executemany("INSERT INTO users VALUES(?, ?, ?);", newUsers)

newCars = [(1,  'Х045ЕР777', 'ВАЗ 2106', 1), 
      (2, 'К555МС55', 'BMW X3?', 1), 
      (3, 'О751АА98', 'Ford Focus 3', 3), 
      (4, 'Е060КХ177', 'Ford Focus 5', 4), 
      (5, 'Е536КХ177', 'Ford Focus 5', 2)]
cursor.executemany("INSERT INTO cars VALUES(?, ?, ?, ?);", newCars)
con.commit()

query = "SELECT * FROM users INNER JOIN cars ON cars.userId = users.userId;"
cursor.execute(query)
data = cursor.fetchall()
print(data)