/* 01 - Sua empresa está fazendo um levantamento de quantos clientes estão cadastrados nos estados, porém, faltou levantar os dados do estado do Rio Grande do Sul.
Então você deve Exibir o nome de todos os clientes cujo estado seja ‘RS’. */
SELECT name FROM Customers WHERE state = 'RS';

/* 02 - A empresa fará um evento comemorando os 20 anos de mercado, e para isso faremos uma grande comemoração na cidade de Porto Alegre. Queremos também convidar todos os nossos clientes que estão cadastrados nessa cidade.
O seu trabalho é nos passar os nomes e os endereços dos clientes que moram em 'Porto Alegre', para entregar os convites pessoalmente. */
SELECT name, street FROM Customers WHERE city = 'Porto Alegre';

/* 03 - O setor financeiro da empresa precisa de um relatório que mostre o código e o nome dos produtos cujo preço são menores que 10 ou maiores que 100. */
SELECT id, name FROM Products WHERE price < 10 OR price > 100;

/* 04 - O setor financeiro precisa de um relatório sobre os fornecedores dos produtos que vendemos. Os relatórios contemplam todas as categorias, mas por algum motivo, os fornecedores dos produtos cuja categoria é a executiva, não estão no relatório.
Seu trabalho é retornar os nomes dos produtos e dos fornecedores cujo código da categoria é 6. */
SELECT p.name, f.name
FROM Products p, Providers f
WHERE p.id_providers = f.id AND p.id_categories = 6;

/* 05 - Quando os dados foram migrados de Banco de Dados, houve um pequeno mal-entendido por parte do antigo DBA.
Seu chefe precisa que você exiba o código e o nome dos produtos, cuja categoria inicie com 'super'. */
SELECT p.id, p.name
FROM Products p, Categories c
WHERE c.name LIKE 'super%' AND p.id_categories = c.id;

/* 06 - Todos os meses a empresa pede um relatório das cidades que os fornecedores estão cadastrados. Dessa vez não vai ser diferente, faça uma consulta no Banco de Dados que retorne todas as cidades dos fornecedores, mas em ordem alfabética.
OBS: Você não deve mostrar cidades repetidas. */
SELECT city
FROM Providers
ORDER BY city ASC;

/* 07 - O setor financeiro da nossa empresa, está querendo saber os menores e maiores valores dos produtos, que vendemos.
Para isso exiba somente o maior e o menor preço da tabela produtos. */
SELECT MAX(price), MIN(price) FROM Products;


/* 08 - Como de costume o setor de vendas está fazendo uma análise de quantos produtos temos em estoque, e você poderá ajudar eles.
Então seu trabalho será exibir o nome e a quantidade de produtos de cada uma categoria. */
SELECT c.name, SUM(p.amount) AS sum
FROM  Products p, Categories c 
WHERE p.id_categories = c.id
GROUP BY c.name;

/* 09 - Na empresa que você trabalha está sendo feito um levantamento sobre os valores dos produtos que são comercializados.
Para ajudar o setor que está fazendo esse levantamento você deve calcular e exibir o valor médio do preço dos produtos. OBS: Mostrar o valor com dois números após o ponto. */
SELECT ROUND(AVG(price), 2)
FROM Products;

/* 10 - Uma Vídeo locadora contratou seus serviços para catalogar os filmes dela. Eles precisam que você selecione o código e o nome dos filmes cuja descrição do gênero seja 'Action'. */
SELECT m.id, name
FROM Movies m, Genres g
WHERE m.id_genres = g.id AND g.description = 'Action';