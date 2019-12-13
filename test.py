import sqlite3
from password import nickname_available, retrieve_account, update_account
from password import show_nicknames, delete_account


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
# the output should be nickname_test, username_test, password_test
retrieve_account('nickname_test', cursor)
# this should test the show_nicknames function
# the output shoulld only have one nickname which is nickname_test
print('\ntesting show_nicknames:')
show_nicknames(cursor)
# this should test the delete_function
# i am going to run show_nicknames after I delete the nickname_test
# to show that it sucessfully deleted the account
delete_account('nickname_test', cursor)
# the output should be blank because I deleted the only account in the database
print('\ntesting delete_account:')
show_nicknames(cursor)
