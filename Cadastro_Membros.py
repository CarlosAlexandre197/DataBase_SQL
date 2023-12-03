'''Cadastro de Visitantes ADSAM 317 2024'''

print('Vamos começar!!!')
id = input('Data: ')
nome = input('Nome: ')
endereco = input('Endereço: ')
cidade = input('Cidade: ')
telefone = input('Telefone: ')
whatsapp = input('Whatsapp: ')
visitas = input('Deseja receber visitas? ')
convertido = input('É novo convertido? ')

import sqlite3

conexao = sqlite3.connect('Cadastro_de_Membros.DB')
cursor = conexao.cursor()

cursor.execute("CREATE TABLE Cadastro_de_Membros (id TEXT, Nome TEXT, Endereço TEXT, Cidade TEXT, Telefone TEXT, Whatsapp TEXT, Visitas TEXT, Convertido)")
planilha_de_dados = ("INSERT INTO Cadastro_de_Membros (id, Nome, Endereço, Cidade, Telefone, Whatsapp, Visitas, Convertido) VALUES(?, ?, ?, ?, ?, ?, ?, ?)")
valores = [id, nome, endereco, cidade, telefone, whatsapp, visitas, convertido]

cursor.execute(planilha_de_dados, valores)
conexao.commit()
print('<<<Dados inseridos com sucesso!>>>')
conexao.close