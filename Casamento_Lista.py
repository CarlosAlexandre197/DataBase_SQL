'''Programa para a criação do Banco de Dados da Lista de Convidados do meu Casamento!'''

import sqlite3

banco = sqlite3.connect('casamento.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE lista_casamento (id integer, orgao text, convidados text)")

cursor.execute("INSERT INTO lista_casamento VALUES (12, 'Igreja', 'Pastor' )")

#cursor.execute("DELETE from lista_casamento WHERE id = 1") # deletando um item da lista

#cursor.execute("UPDATE lista_casamento SET id = 3 WHERE convidados = 'Graziele'") # atualizando um campo da lista
 
banco.commit()

banco.close()
