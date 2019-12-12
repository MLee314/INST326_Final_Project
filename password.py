#!/usr/bin/env python3

import csv
import sqlite3

menu = '''Do you want to:
1. Store a password
2. Retrieve a password
3. Quit'''

def nickname_available(nickname, cursor):
    cursor.execute('''SELECT * FROM passwords ''')
    if cursor.fetchall():
        return True
    else:
        return False

def main():
    conn = sqlite3.connect('password.db')
    cursor = conn.cursor()

    print('Welome to Password Saver')
    print(menu)
    user_input = input("Enter a number: ")

    while user_input != '3':
        if user_input == '1':
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
        elif user_input == '2':
            nickname = input('Enter the nickname of the password you want to retrieve: ')
            print(type(nickname))
            cursor.execute('''SELECT * FROM passwords ''').fetchall()
        print(menu)
        user_input = input("Enter a number: ")

    print('Goodbye!')
    conn.commit()
    conn.close()
if __name__ == '__main__':
    main()