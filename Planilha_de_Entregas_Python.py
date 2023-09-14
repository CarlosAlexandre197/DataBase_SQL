'''Planilha de Entregas Escritório 14/09/2023'''

print('Vamos começar!!!')
id = input()
data = input('Data: ')
taguatinga = int(input('Quantidade Taguatinga? '))
ceilandia = int(input('Quantidade Ceilândia? '))
omni_channel = int(input('Quantidade OMNI Channel? '))
assinatura = input('Assinatura? ')
total = taguatinga + ceilandia + omni_channel


import sqlite3

conexao = sqlite3.connect('Planilha_Setembro.2023.DB')
cursor = conexao.cursor()

cursor.execute("CREATE TABLE Planilha_de_Entregas (id INTEGER NOT NULL PRIMARY KEY, Data TEXT, Taguatinga INTEGER, Ceilândia INTEGER, Omni_Channel INTEGER, Assinatura VARCHAR(25), Total TEXT)")
planilha_de_dados = ("INSERT INTO Planilha_de_Entregas (id, Data, Taguatinga, Ceilândia, Omni_Channel, Assinatura, Total) VALUES(?, ?, ?, ?, ?, ?, ?)")
valores = [id, data, taguatinga, ceilandia, omni_channel, assinatura, total]

cursor.execute(planilha_de_dados, valores)
conexao.commit()
print('<<<Dados inseridos com sucesso!>>>')
conexao.close
