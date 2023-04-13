import sqlite3

banco_db = sqlite3.connect('primeiro_banco.db')

cursor = banco_db.cursor()

cursor.execute('CREATE table pessoas (nome text, idade integer, email text)')

cursor.execute('INSERT into pessoas values ("Alexandre", 35, "alexandre191@gmail.com")')

banco_db.commit()

cursor.execute('SELECT * from pessoas')
print(cursor.fetchall())