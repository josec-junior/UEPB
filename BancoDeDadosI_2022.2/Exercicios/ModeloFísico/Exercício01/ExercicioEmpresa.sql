CREATE SCHEMA Empresa;

USE Empresa;

CREATE TABLE Empregados (
    matricula INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    supervisor INT,
    PRIMARY KEY(matricula),
    FOREIGN KEY(supervisor) REFERENCES Empregados(matricula)
);

CREATE TABLE Dependentes (
    empregado INT NOT NULL,
    nome_dependente VARCHAR(100) NOT NULL,
    parentesco VARCHAR(20) NOT NULL,
    FOREIGN KEY(empregado) REFERENCES Empregados(matricula),
    PRIMARY KEY(empregado, nome_dependente)
);

CREATE TABLE Departamentos (
    codigo INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    gerente INT NOT NULL,
    PRIMARY KEY(codigo),
    FOREIGN KEY(gerente) REFERENCES Empregados(matricula)
);

ALTER TABLE Empregados ADD codigo_departamento INT;
ALTER TABLE Empregados ADD CONSTRAINT FOREIGN KEY(codigo_departamento) REFERENCES Departamentos(codigo);

CREATE TABLE Projetos (
    codigo INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    codigo_departamento INT NOT NULL,
    PRIMARY KEY(codigo),
    FOREIGN KEY(codigo_departamento) REFERENCES Departamentos(codigo)
);

CREATE TABLE Trabalhos (
    empregado INT NOT NULL,
    codigo_projeto INT NOT NULL,
    horas INT NOT NULL,
    PRIMARY KEY(empregado, codigo_projeto),
    FOREIGN KEY(empregado) REFERENCES Empregados(matricula),
    FOREIGN KEY(codigo_projeto) REFERENCES Projetos(codigo)
);

INSERT INTO Empregados (nome, salario) VALUES ("João", 2500.00);
INSERT INTO Empregados (nome, salario) VALUES ("Maria", 2500.00);
INSERT INTO Empregados (nome, salario) VALUES ("Carlos", 4500.00);
INSERT INTO Empregados (nome, salario) VALUES ("Joaquim", 4500.00);

INSERT INTO Departamentos (nome, gerente) VALUES ("Financeiro", 4);
INSERT INTO Departamentos (nome, gerente) VALUES ("Vendas", 3);

UPDATE Empregados
SET supervisor = 4, codigo_departamento = 1 WHERE matricula = 1;

UPDATE Empregados
SET supervisor = 3, codigo_departamento = 2 WHERE matricula = 2;

UPDATE Empregados
SET supervisor = NULL, codigo_departamento = 2 WHERE matricula = 3;

UPDATE Empregados
SET supervisor = NULL, codigo_departamento = 1 WHERE matricula = 4;

INSERT INTO Dependentes (empregado, nome_dependente, parentesco) VALUES (2, "Marcos", "Filho");
INSERT INTO Dependentes (empregado, nome_dependente, parentesco) VALUES (2, "Luís", "Filho");
INSERT INTO Dependentes (empregado, nome_dependente, parentesco) VALUES (3, "Ana", "Cônjuge");

INSERT INTO Projetos (nome, codigo_departamento) VALUES ("Venda Fácil", 2);
INSERT INTO Projetos (nome, codigo_departamento) VALUES ("MaxLucro", 1);
INSERT INTO Projetos (nome, codigo_departamento) VALUES ("Cliente Ouro", 1);

INSERT INTO Trabalhos (empregado, codigo_projeto, horas) VALUES (1, 2, 12);
INSERT INTO Trabalhos (empregado, codigo_projeto, horas) VALUES (1, 3, 12);
INSERT INTO Trabalhos (empregado, codigo_projeto, horas) VALUES (2, 1, 12);
INSERT INTO Trabalhos (empregado, codigo_projeto, horas) VALUES (2, 2, 12);
INSERT INTO Trabalhos (empregado, codigo_projeto, horas) VALUES (4, 2, 12);
INSERT INTO Trabalhos (empregado, codigo_projeto, horas) VALUES (4, 3, 12);