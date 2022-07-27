import sqlite3 as sq

BaseName = "TrainingAlarmBase.db"


# Инициализация базы данных
def InitialAlarmBase():
    db = sq.connect(BaseName)
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS alarms(
        id INTEGER PRIMARY KEY,
        type TEXT,
        day TEXT,
        time TEXT,
        place TEXT);
    """)
    db.commit()
    db.close()


# Чтение базы данных
def AlarmBaseReading():
    db = sq.connect(BaseName)
    cur = db.cursor()
    cur.execute("SELECT * FROM alarms;")
    all_results = cur.fetchall()
    db.close()
    return all_results


# Сохранение данных в базу данных
def DataSave(data):
    base = sq.connect(BaseName)
    cursor = base.cursor()

    #Добавление новых элементов
    if(data[0] == ''):
        cursor.execute("""INSERT INTO alarms(type, day, time, place) VALUES (?,?,?,?)""", data[1:])
    base.commit()
    base.close()
