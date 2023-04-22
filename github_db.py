'''Lista de alimentos do nosso Chá de Panela'''

import sqlite3

banco = sqlite3.connect('github.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE lista (id integer, quantidade integer, descricao text, situacao text)")

cursor.execute("INSERT INTO lista VALUES (7, 3, 'Farinha de Mandioca kg', 'pendente')")

cursor.execute("DELETE from lista WHERE id = 6") # deletando um item da lista

cursor.execute("UPDATE lista SET descricao = 'Farinha de Mandioca 1kg' WHERE id = 7") # atualizando um campo da lista
 
banco.commit()

banco.close()
