#!/usr/bin/env python3

import csv
import sqlite3

menu = '''Do you want to:
1. Store an account
2. Retrieve account information
3. Update an existing account
4. Delete an account
5. Quit'''

# This function retrieve all of the information given a nickname
def retrieve_account(nickname, cursor):
    cursor.execute('''SELECT * FROM passwords WHERE nickname = '{}' '''.format(nickname))
    records = cursor.fetchall()
    print("\nNickname: " + str(records[0][0]) +
            "\nUsername: " + str(records[0][1]) +
            "\nPassword: " + str(records[0][2]))

# This function checks if a nickname is already present in the database.
def nickname_available(nickname, cursor):
    cursor.execute('''SELECT nickname FROM passwords''')
    list = cursor.fetchall()
    for i in list:
        if (nickname == ''.join(i)):
            return False
    return True

def main():
    conn = sqlite3.connect('password.db')
    cursor = conn.cursor()

    print('Welome to Password Saver')
    print('\n' + menu)
    user_input = input("Enter a number: ")

    while user_input != '5':
        # STORE PASSWORD
        if user_input == '1':
            # create table for first time users
            cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                    (nickname TEXT,
                    username TEXT,
                    password TEXT)''')

            nickname = input('Enter a nickname: ')
            if nickname_available(nickname, cursor):
                username = input('Enter a username or email address: ')
                password = input('Enter a password: ')

                cursor.execute('INSERT INTO passwords VALUES (?, ?, ?)',
                            (nickname, username, password))

            conn.commit()
        # RETRIEVE PASSWORD
        elif user_input == '2':
            nickname = input('Enter the nickname of the account: ')
            retrieve_account(nickname, cursor)

        print('\n' + menu)
        user_input = input("Enter a number: ")

    print('\nGoodbye!')
    conn.commit()
    conn.close()
if __name__ == '__main__':
    main()
