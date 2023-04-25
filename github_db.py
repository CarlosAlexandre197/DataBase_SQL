'''Lista de alimentos do nosso Chá de Panela'''

import sqlite3

banco = sqlite3.connect('github.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE lista (id integer, quantidade integer, descricao text, situacao text)")

#cursor.execute("INSERT INTO lista VALUES (9, 6, '', 'OK')")

#cursor.execute("DELETE from lista WHERE descricao = 'Colher Descartável 50un' ") # deletando um item da lista

cursor.execute("UPDATE lista SET quantidade = 8 WHERE id = 4") # atualizando um campo da lista
 
banco.commit()

banco.close()
