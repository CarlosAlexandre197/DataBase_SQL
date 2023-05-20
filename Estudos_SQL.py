print('Cadastro de Pedidos para entrega')
id = int(input('Pedido: '))
loja = int(input('Código: '))
destinatario = input('Cliente: ')
telefone = int(input('Telefone: '))
uf = input('UF: ')
municipio = input('Município: ')
bairro = input('Bairro: ')
numero = int(input('Número: '))
endereco = input('Endereço: ')
cep = int(input('CEP: '))
complemento = input('Complemento: ')
data_limite = (input('Data_Limite: '))
data_da_carga = input('Data_da_Carga: ')
volumes = int(input('Volumes: '))
valor_nf = (input('Valor_NF: '))

import sqlite3

conexao = sqlite3.connect('estudos.db')
cursor = conexao.cursor()
#cursor.execute("CREATE TABLE Cadastro_de_Entregas (id INTEGER NOT NULL PRIMARY KEY, Loja INTEGER, Destinatário VARCHAR(25), Telefone TEXT, UF TEXT, Município VARCHAR(25), Bairro VARCHAR(25), Número INTEGER, Endereço VARCHAR(250), CEP TEXT, Complemento TEXT, Data_Limite TEXT, Data_da_Carga TEXT, Volumes INTEGER, Valor_NF TEXT)")
banco_de_dados = ("INSERT INTO Cadastro_de_Entregas (id, Loja, Destinatário, Telefone, UF, Município, Bairro, Número, Endereço, CEP, Complemento, Data_Limite, Data_da_Carga, Volumes, Valor_NF) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
valores = [id, loja, destinatario, telefone, uf, municipio, bairro, numero, endereco, cep, complemento, data_limite, data_da_carga, volumes, valor_nf]

cursor.execute(banco_de_dados, valores)
conexao.commit()
print('<<<Dados inseridos com sucesso!>>>')
conexao.close