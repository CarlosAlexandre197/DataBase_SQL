import sqlite3

banco = sqlite3.connect('github.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE lista (id integer, quantidade integer, descricao text, situacao text)")

cursor.execute("INSERT INTO lista VALUES (4, 2, 'Óleo de soja 900ml', 'OK')")

cursor.execute("DELETE from lista WHERE id = 4") # deletando um item da lista
 
banco.commit()

banco.close()
