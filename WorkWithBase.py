import sqlite3 as sq

BaseName = "TrainingAlarmBase.db"


def InitialAlarmBase():
    db = sq.connect(BaseName)
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS alarms(
       Номер INT,
       День недели TEXT,
       Время TEXT,
       Сообщение TEXT);
    """)
    db.commit()
    db.close()