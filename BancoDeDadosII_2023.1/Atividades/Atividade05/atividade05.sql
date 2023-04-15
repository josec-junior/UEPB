/* Questão 01 - Crie uma função para reajustar salários. O reajuste deve ser aplicado para todos os funcionários, e deve seguir a seguinte tabela:
    5% de reajuste para os funcionários que não estão envolvidos em nenhuma atividade de projeto;
    10% de reajuste para os funcionários que estão envolvidos em até 2 atividades de projeto;
    15% de reajuste para os funcionários que estão envolvidos em pelo menos 3 atividades de projeto. */

CREATE OR REPLACE FUNCTION reajustar_salarios() RETURNS VOID AS
$$
BEGIN
	UPDATE Funcionarios 
	SET salario = CASE
		WHEN funcionarios.id NOT IN (
			SELECT DISTINCT(f.id)
			FROM Funcionarios f
			JOIN Projetos p
			ON f.id = p.funcionario_responsavel_id
			JOIN AtividadesProjetos ap
			ON p.id = ap.projeto_id
		) THEN
			salario + salario * 0.05
		WHEN funcionarios.id IN (
			SELECT DISTINCT(f.id)
			FROM funcionarios f
			JOIN projetos p
			ON f.id = p.funcionario_responsavel_id
			JOIN AtividadesProjetos ap
			ON p.id = ap.projeto_id
			GROUP BY f.id
			HAVING COUNT(ap.atividade_id) <= 2
		) THEN
			salario + salario * 0.1
		ELSE
			salario + salario * 0.15
	END;
END;
$$ LANGUAGE plpgsql;

-- Questão 02 - Execute o reajuste criado na questão 1.

SELECT reajustar_salarios();

/* Questão 03 - Modifique a tabela Departamentos, acrescentando uma coluna chamada total_atividades (numeric).
Essa coluna deve ser preenchida para todos os departamentos, contendo o número de atividades desenvolvidas, somando todos os projetos daquele departamento específico. */

ALTER TABLE Departamentos
ADD total_atividades NUMERIC;

UPDATE Departamentos
SET total_atividades = total_atividades_query.total_atividades FROM
	(SELECT p.departamento_id, COUNT(ap.atividade_id) AS total_atividades
	FROM AtividadesProjetos ap JOIN
	Projetos p
	ON ap.projeto_id = p.id
	GROUP BY p.departamento_id) AS total_atividades_query
WHERE id = total_atividades_query.departamento_id;

-- Questão 04 -  Crie um gatilho na tabela AtividadesProjetos, para que cada vez que uma nova linha seja inserida; a tabela Departamentos tenha o seu campo total_atividades ajustado no departamento responsável pelo projeto no qual foi realizada uma nova atividade.

CREATE OR REPLACE FUNCTION ajustar_total_atividades() RETURNS TRIGGER AS
$$
BEGIN
	UPDATE Departamentos
	SET total_atividades = total_atividades + 1
	WHERE id = (SELECT p.departamento_id
			   FROM Projetos p
			   WHERE p.id = NEW.projeto_id);
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_atualizar_total_atividades
AFTER INSERT ON AtividadesProjetos
FOR EACH ROW
EXECUTE FUNCTION ajustar_total_atividades();

INSERT INTO AtividadesProjetos VALUES()

-- Questão 05 - Crie uma tabela chamada Prêmios (id, funcionario_id, data, valor).

CREATE TABLE Premios (
	id SERIAL,
	funcionario_id INTEGER,
	data DATE,
	valor NUMERIC,
	PRIMARY KEY(id),
	FOREIGN KEY(funcionario_id) REFERENCES Funcionarios(id)
);

-- Questão 06 - Crie um gatilho na tabela AtividadesProjetos, para que cada vez que uma nova linha seja inserida, caso o funcionário responsável pelo projeto tenha atingido 3 atividades, receba um prêmio de 20% do salário (inserido na tabela prêmio).

CREATE OR REPLACE FUNCTION receber_trofeu() RETURNS TRIGGER AS
$$
DECLARE
	funcionario_id INT;
	atividades INT;
	valor NUMERIC;
BEGIN
	SELECT p.funcionario_responsavel_id
	FROM Projetos p
	WHERE p.id = new.projeto_id INTO funcionario_id;
	
	SELECT COUNT(ap.atividade_id)
	FROM AtividadesProjetos ap
	WHERE ap.projeto_id = new.projeto_id INTO atividades;
	
	SELECT salario
	FROM Funcionarios
	WHERE id = funcionario_id INTO valor;

	IF (atividades = 3) THEN
		INSERT INTO Premios(funcionario_id, data, valor) VALUES
		(funcionario_id, NOW(), valor * 0.2);
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_receber_trofeu
AFTER INSERT ON AtividadesProjetos
FOR EACH ROW
EXECUTE FUNCTION receber_trofeu();

-- Questão 07 - Crie uma visão chamada Total_premios_2023, que contenha o nome do funcionário e o total em prêmios que ele tem a receber em 2023.

CREATE OR REPLACE VIEW total_premios_2023 AS
SELECT nome, SUM(valor) AS total_a_receber
FROM Funcionarios f
JOIN Premios p
ON f.id = p.funcionario_id
WHERE data BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY nome;

SELECT * FROM total_premios_2023;