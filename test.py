import sqlite3
from password import nickname_available, retrieve_account, update_account

# TESTING
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cq = '''CREATE TABLE IF NOT EXISTS passwords (
        nickname TEXT, username TEXT, password TEXT
        )'''
cursor.execute(cq)

iq = '''INSERT INTO passwords VALUES(
        'nickname_test',
        'username_test',
        'password_test'
)'''
cursor.execute(iq)

# tests if a nickname already exists in the database
assert nickname_available('nickname_test', cursor) == False
# tests if a nickname doesn't exist in the databse
assert nickname_available('not_in_database', cursor) == True
# this should print nickname, username and password of the specified nickname
retrieve_account('nickname_test', cursor)
