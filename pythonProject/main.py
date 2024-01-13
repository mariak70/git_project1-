import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('coffee.sqlite')
cursor = conn.cursor()

# Запрос к базе данных
cursor.execute("SELECT * FROM coffee")

# Получение результатов запроса
rows = cursor.fetchall()

# Отображение информации о кофе
for row in rows:
    print("ID:", row[0])
    print("Coffee Name:", row[1])
    print("Roast Level:", row[2])
    print("Ground/Whole Bean:", row[3])
    print("Flavor Description:", row[4])
    print("Price:", row[5])
    print("Package Size:", row[6])
    print("\n")

# Закрытие соединения с базой данных
conn.close()
