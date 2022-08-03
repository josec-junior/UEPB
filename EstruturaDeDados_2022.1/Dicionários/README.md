<h1> Dicionários </h1>
<h2> Coleções em Python </h2>
<p>
  - Uma coleção é uma estrutura de dados elaborada para manter múltiplas informações.
  <br>
  - Já estudamos Listas (list), que é uma das coleções disponíveis no Python.
  <br>
  - Na sequência veremos Tuplas e Dicionários.
</p>
<h2> Tuplas </h2>
<p>
  Síntaxe: <em> identificador = (dados) </em>
  <br>
  - Criar uma tupla é semelhante a criar uma lista.
  <br>
  - Basta substituir [] por ().
  <br>
  - A principal diferença entre Tuplas e Listas é o fato de Tuplas serem <strong> imutáveis</strong>. (Não se pode editar uma Tupla).
  <br>
  - Então, por quê não utilizar sempre uma lista?
  <br>
  &rarr; A manipulação de tuplas é mais eficiente, em termos de consumo de memória e processamento.
</p>
<h2> Dicionários </h2>
<p>
  Síntaxe: <em> identificador = {chave: valor, ...} </em>
  <br>
  - Um dicionário é uma coleção que tem suas posições acessíveis atráves de suas chaves.
  <br>
  - Diferente de listas, que têm suas posições acessíveis através de índices.
  <br>
  Exemplo: <em> identificador[chave] = valor </em>
  <br>
  &rarr; Caso a chave não exista, será criada uma nova posição no dicionário.
  <br>
  - Os elementos dentro de um dicionário não são ordenados.
</p>
<h3> Métodos </h3>
<p>
  <ul>
    <li> <em> keys() </em> - Retorna as chaves existentes no dicionário. </li>
    <li> <em> values() </em> - Retorna os valores existentes no dicionário. </li>
    <li> <em> items() </em> - Retorna tuplas contendo (chave, valor). </li>
    <li> <em> pop(chave) </em> - Exclui e retorna o valor correspondente à chave fornecida.
    <li> <em> get(chave, default) </em> - Retorna o valor correspondente à chave fornecida, caso não exista, retorna default. 
  </ul>
</p>
<h3> Exercício </h3>
<p>
  Fazer um programa para contar a quantidade de ocorrências de cada palavra em um texto. Identificar:
  <ol type = "a">
    <li> A palavra que mais ocorre e sua quantidade. </li>
    <li> Uma lista com as 10 palavras mais frequentes. </li>
  </ol>
  <a href = "https://github.com/josec-junior/UEPB/blob/main/EstruturaDeDados_2022.1/Dicion%C3%A1rios/ExercicioDicionario/exerciciodicio.py"> Acesse o exercício </a>
</p>
