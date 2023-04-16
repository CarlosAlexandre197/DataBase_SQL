import sqlite3

banco_db = sqlite3.connect('banco_dados.db')

cursor = banco_db.cursor()

cursor.execute('CREATE table pessoas (nome text, idade integer, email text)')

cursor.execute('INSERT into pessoas values ("Alexandre", 35, "alexandrec191@gmail.com")')

banco_db.commit()

cursor.execute('SELECT * from pessoas')
print(cursor.fetchall())

banco_db execute()