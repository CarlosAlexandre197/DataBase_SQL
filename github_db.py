import sqlite3

banco = sqlite3.connect('github.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE lista (id integer, quantidade integer, descricao text, situacao text)")

cursor.execute("INSERT INTO lista VALUES (4, 2, 'Óleo de soja 900ml', 'OK')")

cursor.execute('SELECT * FROM lista')
 
banco.commit()
banco.close()
