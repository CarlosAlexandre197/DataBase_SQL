'''Exercício'''

import sqlite3

conexao = sqlite3.connect('exercicio.db')

cursor = conexao.cursor()

#cursor.execute("CREATE TABLE cliente (id integer, nome varchar(100), cpf text(11), data_cadastro text(10), endereço text(50))")

cursor.execute("INSERT INTO cliente VALUES (1, 'Danilo', '11111111111', '05/10/2022', 'RIO TINTO')")

conexao.commit()

conexao.close()