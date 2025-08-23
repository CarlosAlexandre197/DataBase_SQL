'''Planilha de Entregas Escritório 2025-08-23'''

print('Vamos começar?')
data = input('Data: ')
taguatinga = int(input('Quantidade Taguatinga? '))
ceilandia = int(input('Quantidade Ceilândia? '))
omni_channel = int(input('Quantidade OMNI Channel? '))
assinatura = input('Assinatura? ')
total = taguatinga + ceilandia + omni_channel


import sqlite3

conexao = sqlite3.connect('Planilha_marco_2024.DB')
cursor = conexao.cursor()

cursor.execute("CREATE TABLE Planilha_de_Entregas (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Data TEXT, Taguatinga INTEGER, Ceilândia INTEGER, Omni_Channel INTEGER, Assinatura VARCHAR(25), Total TEXT)")
planilha_de_dados = ("INSERT INTO Planilha_de_Entregas (Data, Taguatinga, Ceilândia, Omni_Channel, Assinatura, Total) VALUES(?, ?, ?, ?, ?, ?)")
valores = [data, taguatinga, ceilandia, omni_channel, assinatura, total]

cursor.execute(planilha_de_dados, valores)
conexao.commit()
print('<<<Dados inseridos com sucesso!>>>')
conexao.close
