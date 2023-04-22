-- Questão 01 - Crie uma visão materizalizada contendo 3 colunas: nome do projeto, quantidade de atividades realizadas, nome do responsável. Essa visão deve ser criada sem dados;

CREATE MATERIALIZED VIEW projetos_atividades_responsaveis_mat AS
SELECT p.descricao AS nome_projeto, COUNT(ap.atividade_id) AS quantidade_atividades, f.nome AS nome_responsavel
FROM Funcionarios f
JOIN Projetos p
ON f.id = p.funcionario_responsavel_id
JOIN AtividadesProjetos ap
ON p.id = ap.projeto_id
GROUP BY p.descricao, f.nome
WITH NO DATA;

-- Questão 02 - Faça com que a visão seja povoada;

REFRESH MATERIALIZED VIEW projetos_atividades_responsaveis_mat;

-- Questão 03 - Consulte na visão quais os nomes dos projetos com ao menos três atividades realizadas;

SELECT nome_projeto FROM projetos_atividades_responsaveis_mat
WHERE quantidade_atividades >= 3;

-- Questão 04 - Execute "INSERT INTO atividadesprojetos VALUES(3,1,null,null)";

INSERT INTO atividadesprojetos VALUES (3, 1, NULL, NULL);

-- Questão 05 - Refaça a consulta 3. Mudou alguma coisa?

SELECT nome_projeto FROM projetos_atividades_responsaveis_mat
WHERE quantidade_atividades >= 3;

-- Resposta: Não mudou, pois, por se tratar de uma visão materializada, é preciso realizar um refresh para que essa seja atualizada.

-- Questão 06 - Dê um refresh na visão materializada e refaça a consulta 3. Mudou alguma coisa?

REFRESH MATERIALIZED VIEW projetos_atividades_responsaveis_mat;

SELECT nome_projeto FROM projetos_atividades_responsaveis_mat
WHERE quantidade_atividades >= 3;

-- Resposta: Mudou, pois após realizar o refresh, a visão materializada foi atualizada.