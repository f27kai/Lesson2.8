import sqlite3

with sqlite3.connect('students.db') as conn:
    c = conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS students ( 
    имя TEXT VARCHAR(20) NOT NULL,
    фамилия TEXT,
    год_рождения TEXT NOT NULL,
    хобби TEXT NOT NULL,
    баллы_за_дз INT NOT NULL
    )""")

    c.execute(""" INSERT INTO students(имя, фамилия, год_рождения, хобби, баллы_за_дз) VALUES
    (Asan, Asanov, 2004-01-01, playing_footbal, 10),
    (Aygul, Asanova, 2005-01-02, watch_TV, 8),
    (Aybek, Aybekov, 2005-03-04, watch_TV, 12),
    (Ayba, Aybarov, 2006-09-27, watch_TV, 14),
    (Samat, Samatov, 2000-03-27, watch_TV,24),
    (Ruslan, Ruskanov, 1998-02-28, watch_TV, 25)
    """)

    c.execute(""" DELETE FROM rowid % 2 == 0""")

    c.execute(""" SELECT * FROM students """)

    for i in c:
        print(i)
