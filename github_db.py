import sqlite3

banco = sqlite3.connect('github.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE lista (id integer, quantidade integer, descricao text, situacao text)")

cursor.execute("INSERT INTO lista VALUES (5, 30, 'Coxa e sobrecoxa kg', 'pendente')")

cursor.execute("DELETE from lista WHERE id = 5") # deletando um item da lista

cursor.execute("UPDATE lista SET situacao = 'pendente' WHERE id = 5") # atualizando um campo da lista
 
banco.commit()

banco.close()
