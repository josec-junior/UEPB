DROP TABLE IF EXISTS AtividadesProjetos;
DROP TABLE IF EXISTS Projetos;
ALTER TABLE IF EXISTS Funcionarios;
DROP CONSTRAINT FkDepto;
DROP TABLE IF EXISTS Departamentos;
DROP TABLE IF EXISTS Funcionarios;
DROP TABLE IF EXISTS Atividades;

CREATE TABLE Atividades (
   id INT PRIMARY KEY,
   descricao VARCHAR(30) NOT NULL
);

CREATE TABLE Funcionarios (
   id INT PRIMARY KEY,
   nome VARCHAR(30) NOT NULL,
   sexo CHAR(1) NOT NULL CHECK (Sexo IN ('F','M')),
   salario NUMERIC(8,2) NOT NULL,
   departamento_id INT
);

CREATE TABLE Departamentos (
   id INT PRIMARY KEY,
   descricao VARCHAR(30) NOT NULL,
   funcionario_gerente_id INT
);

ALTER TABLE Funcionarios ADD CONSTRAINT FkDepto FOREIGN KEY (departamento_id)
   REFERENCES departamentos (id) ON DELETE SET NULL;

ALTER TABLE Departamentos ADD CONSTRAINT FkFuncionario FOREIGN KEY (funcionario_gerente_id)
   REFERENCES Funcionarios (id) ON DELETE SET NULL;

CREATE TABLE Projetos (
   id INT PRIMARY KEY,
   descricao VARCHAR(30) NOT NULL,
   departamento_id INT REFERENCES Departamentos (id) ON DELETE SET NULL,
   funcionario_responsavel_id INT REFERENCES Funcionarios (id) ON DELETE SET NULL
);

CREATE TABLE AtividadesProjetos (
   projeto_id INT NOT NULL REFERENCES Projetos (id),
   atividade_id INT NOT NULL REFERENCES Atividades (id),
   data_inicio DATE,
   data_fim DATE,
   CONSTRAINT PkAtividadesProjetos PRIMARY KEY (projeto_id, atividade_id)
);

INSERT INTO departamentos
VALUES (1,'Informatica',NULL);

INSERT INTO departamentos
VALUES (2,'Materiais',NULL);

INSERT INTO departamentos
VALUES (3,'Pessoal',NULL);

INSERT INTO Funcionarios
VALUES (1,'Marsell','M',3000,1);

INSERT INTO Funcionarios
VALUES (2,'Cleber','M',3500,1);

INSERT INTO Funcionarios
VALUES (3,'Charles','M',2500,2);

INSERT INTO Funcionarios
VALUES (4,'Paula','F',3000,3);

INSERT INTO Funcionarios
VALUES (5,'Gutemberg','M',4000,2);

INSERT INTO Funcionarios
VALUES (6,'Felipe','M',2000,3);

INSERT INTO Funcionarios
VALUES (7,'Fernando','M',2500,3);

UPDATE departamentos
SET funcionario_gerente_id = 1
WHERE id = 1;

UPDATE departamentos
SET funcionario_gerente_id = 5
WHERE id = 2;

UPDATE departamentos
SET funcionario_gerente_id = 4
WHERE id = 3;

INSERT INTO Projetos
VALUES (1, 'Alfa', 1, 2);

INSERT INTO Projetos
VALUES (2, 'Beta', 1, NULL);

INSERT INTO Projetos
VALUES (3, 'Gama', 3, 7);

INSERT INTO Atividades
VALUES (1, 'Projeto Arquitetural');

INSERT INTO Atividades
VALUES (2, 'Desenvolvimento de codigo');

INSERT INTO Atividades
VALUES (3, 'Testes de unidade');

INSERT INTO Atividades
VALUES (4, 'Testes de usabilidade');

INSERT INTO Atividades
VALUES (5, 'Contratacao de funcionarios');

INSERT INTO Atividades
VALUES (6, 'Compra de material');

INSERT INTO Atividades
VALUES (7, 'Implantacao do produto');

INSERT INTO Atividades
VALUES (8, 'Busca por recursos');

INSERT INTO AtividadesProjetos
VALUES (1, 1, NULL, NULL);

INSERT INTO AtividadesProjetos
VALUES (1, 2, NULL, NULL);

INSERT INTO AtividadesProjetos
VALUES (1, 3, NULL, NULL);

INSERT INTO AtividadesProjetos
VALUES (2, 1, NULL, NULL);

INSERT INTO AtividadesProjetos
VALUES (2, 2, NULL, NULL);

INSERT INTO AtividadesProjetos
VALUES (2, 3, NULL, NULL);

INSERT INTO AtividadesProjetos
VALUES (2, 4, NULL, NULL);

INSERT INTO AtividadesProjetos
VALUES (2, 7, NULL, NULL);

INSERT INTO AtividadesProjetos
VALUES (3, 8, NULL, NULL);

INSERT INTO AtividadesProjetos
VALUES (3, 5, NULL, NULL);
