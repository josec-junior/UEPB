<h1> Hash </h1>
<h2> Transformação de Chave </h2> 
<p>
	- Os métodos de pesquisa vistos anteriormente são baseados na <strong> Comparação de Chaves</strong>.
  <br>
	- O método de <em> Hashing </em> é baseado na <strong> Transformação de Chaves</strong>.
  <br>
  &rarr; Os registros em uma tabela são diretamente endereçados a partir de uma transformação aritmética, a qual é feita em duas etapas:
  <ol>
    <li> Computar o valor da função Hashing (função de transformação), que transforma a chave em um endereço da tabela. </li>
    <li> Evitar colisões, uma vez que mais de uma chave podem ser transformadas em um mesmo endereço. </li>
  </ol>
  - Considerando chaves como inteiros de 1 a <em> n</em>, pode-se armazenar o registro com chave <em> i </em> na posição <em> i </em> da tabela.
  <br>
  - Outros tipos de chaves não são tão diretos.
  <br>
  <br>
  <ul>
    <li> Suponha uma tabela com capacidade para M = 97 chaves. </li>
    <li> Cada chave pode ser um número decimal de quatro dígitos. </li>
    <ul>
      <li> N = 10.000 chaves possíveis. </li>
    </ul>
    <li> A função de transformação não pode ser um para um. </li>
    <li> Meso que haja muito menos que 97 registros, colisões deverão ocorrer; logo, devem ser tratadas de alguma forma. </li>
  </ul>
</p>
<h2> Probabilidade de Colisões </h2>
<h3> Paradoxo do aniversário </h3>
<p>
  - Feller, 1968.
  <br>
  - Num grupo de 23 pessoas unidas ao acaso, a chance de duas fazerem aniversário no mesmo dia é maior que 50%.
  <br>
  &rarr; Com uma função de transformação que enderece 23 chaves randômicas em uma tabela com 365 registros, temos probabilidade maior do que 50% de haver colisão.
</p>
<h2> Funções de Transformação </h2>
<p>
  - Uma função deve mapear chaves em inteiros dentro do intervalo [0, ... , M - 1], no qual <em> M </em> é o tamanho da tabela.
  <br>
  - Uma função ideal deve ser:
  <ol>
    <li> Simples de ser computada; </li>
    <li> Para cada chave de entrada, as saídas possíveis têm a mesma probabilidade de ocorrer. </li>
  </ol>
  - A primeira coisa a fazer é transformar chaves não numéricas em núnmeros.
  <br>
  - Várias funções de transformação foram estudadas.
  <br>
  - Um dos métodos que funciona bem é o resto da divisão por <em> M</em>.
  <br>
  <br>
  <ul>
    <li> <em> h(K) = K mod M. </em> </li>
    <li> Onde <em> K </em> é um inteiro correspondente à chave. </li>
  </ul>
</p>
<h2> Listas Encadeadas </h2>
<p>
  - Uma das formas de evitar colisões é construir listas lineares encadeadas para cada endereço da tabela.
  <br>
  &rarr; Todas as chaves com um mesmo endereço são encadeadas em uma mesma lista.
  <br>
  Exemplo:
  <ul>
    <li> Inserção das chaves P E S Q U I S A na tabela, onde: </li>
    <ul>
      <li> A <em> i</em>-ésima letra do alfabeto é representada pelo número <em> i. </em>
      <li> A função de transformação h(Chave) = Chave mod M, para M = 7.
    </ul>
  </ul>
</p>
