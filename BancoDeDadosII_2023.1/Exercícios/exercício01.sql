-- 1 - Qual o total de funcionários da empresa?
SELECT COUNT(*) AS total_funcionarios FROM Funcionarios;

-- 2 - Qual a média salarial da empresa?
SELECT AVG(salario) AS media_salarial FROM Funcionarios;

-- 3 - Qual o total de funcionários e a média salarial por departamento?
SELECT AVG(salario) AS media_salarial, COUNT(*) AS total_funcionarios
FROM Funcionarios
GROUP BY departamento_id;

-- 4 - Selecione o nome dos funcionários que são gerentes ou que ganham acima de R$ 3.000,00.
SELECT DISTINCT(nome)
FROM Funcionarios F, Departamentos D
WHERE F.id = D.funcionario_gerente_id OR salario > 3000;

-- 5 - Selecione os projetos que tenham no mínimo 3 atividades realizadas.
SELECT descricao
FROM Projetos, AtividadesProjetos
WHERE id = projeto_id GROUP BY descricao HAVING COUNT(projeto_id) >= 3;
