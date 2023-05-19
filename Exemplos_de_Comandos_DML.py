'''Exemplos de Comandos DML'''

'''CREATE TABLE fornecedor (
    id INT,
    nome VARCHAR(150) NOT NULL,
    endereco VARCHAR(150),
    produtos VARCHAR(20)
);

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (1, 'Empresa de Leite ParmaLeite', 'Rua dos Leites, 23', 'leite');

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (2, 'Peixaria Abril', 'Rua dos Leites, 25', 'peixe');

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (3, 'Açougue Legal', 'Rua dos Leites, 30', 'carnes');

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (4, 'Açougue Novo', 'Rua dos Leites, 35', 'carnes');

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (3, 'Padaria do Pão', 'Rua dos Leites, 40', 'pão');

INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (4, 'Marcenaria Martelo', 'Rua dos Leites, 45', 'móveis');

UPDATE fornecador set endereco = 'Rua dos Peixes, 26'
where endereco = 'Rua dos Leites, 25';

SELECT * from fornecedor;

SELECT * from fornecedor;
WHERE produtos = 'carnes';

 DELETE FROM fornecedor; 
 WHERE id = 1;'''
