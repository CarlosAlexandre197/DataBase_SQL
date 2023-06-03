'''Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. 
As tabelas devem compreender as seguintes funcionalidades:'''

'''>>>As tarefas devem ser divididas em “categorias”;
Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
As restrições/relacionamentos devem fazer sentido.<<<'''

import sqlite3

banco = sqlite3.connect('exercio02.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE Caminhada (nome varchar(25), data varchar(10), categoria varchar(100), status_final varchar(100))")

cursor.execute("INSERT INTO Caminhada VALUES ('Caminhada no Parque de Águas Claras', '15/05/2023', 'Exercícios', 'Pendente', 1)")

cursor.execute("ALTER TABLE Caminhada ADD COLUMN id interger ")

cursor.execute("UPDATE Caminhada SET categoria = 'Exercícios Físicos'") 

cursor.execute("ALTER TABLE Caminhada DROP COLUMN id")

cursor.execute("DELETE from Caminhada WHERE categoria = 'Exercícios'") 

'''Crie um programa em Python que gere tabelas para uma aplicação de eventos. Elas devem compreender as seguintes funcionalidades:'''

'''Eventos devem ter título, data e local, além da referência ao organizador;
O organizador deve ter nome, email e cpf;
As restrições/relacionamentos devem fazer sentido.'''

cursor.execute("CREATE TABLE Casamento (Evento varchar(50), Data_Local varchar(100), Referência_Organizador varchar(250))")

cursor.execute("INSERT INTO Casamento VALUES ('Casamento de Alexandre & Ester', '08/07/2023 Vicente Pires/Salão Vip-Ceilândia Sul', 'Rose mais de 25 no mercado de Eventos', 1)")

cursor.execute("ALTER TABLE Casamento ADD COLUMN id interger")

cursor.execute("UPDATE Casamento SET Referência_Organizador = 'Rose mais de 25 anos no mercado de Eventos.' ") 

cursor.execute("CREATE TABLE Organizador (id interger AUTO_INCREMENT, Nome varchar(20), email varchar(20), CPF varchar(11))")

cursor.execute("DELETE from Casamento WHERE Referência_Organizador = 'Rose mais de 25 anos no mercado de Eventos.'") 

cursor.execute("INSERT INTO Organizador VALUES ('', 'Rose', 'rose@.rose', '11111111111')")

banco.commit()
banco.close()
