/* Selecionar a matrícula e o nome de todos os empregados que trabalham no departamento 2 */
SELECT matricula, nome FROM Empregados WHERE codigo_departamento = 2;

/* Selecionar a matrícula e o nome dos empregados do departamento 2 que ganham mais de três mil reais */
SELECT matricula, nome FROM Empregados WHERE codigo_departamento = 2 AND salario > 3000;

/* Selecionar a matrícula e o nome de todos os empregados */
SELECT matricula, nome FROM Empregados;

/* Selecionar as informações sobre os empregados do departamento dois */
SELECT * FROM Empregados WHERE codigo_departamento = 2;

/* Selecionar a matrÍcula e o nome de todos os empregados, renomeando somente atributo nome para NomeEmpregado. */
SELECT matricula, nome AS nome_empregado FROM Empregados;

/* Calcule como ficaria o novo salário de cada empregado caso eles recebessem um aumento de 15%, recuperando a sua matricula, nome e o novo salário reajustado. */
SELECT matricula, nome, salario + salario * 0.15 AS salario_reajustado FROM Empregados;

/* Selecione o nome dos empregados que trabalham no departamento de Vendas */
SELECT nome FROM Empregados WHERE codigo_departamento = 2;

/* Recupere a matrícula, o nome e o nome do supervisor de cada empregado */
SELECT E.Matricula, E.Nome, S.Nome AS Supervisor FROM Empregado E, Empregado S WHERE E.Supervisor = S.Matricula;

/* Recupere o nome de todos os empregados que não tem supervisor */
SELECT Nome FROM Empregado WHERE Supervisor IS NULL;

/* Recupere o nome de todos os empregados que possuem um supervisor */
SELECT Nome FROM Empregado WHERE Supervisor IS NOT NULL;