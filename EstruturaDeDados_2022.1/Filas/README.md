<h1> Filas </h1>
<h2> Pilhas e Filas </h2>
<p>
  - São dois tipos abstratos de dados sequenciais;
  <br>
  - Se diferenciam de Listas, pois possuem restrições de acesso;
  <br>
  - Ou seja, <strong> nem toda operação é permitida </strong> em uma Pilha ou Fila.
</p>
<h2> Filas </h2>
<p>
  Estrutura FiFo - <em> First in, First out </em>
  <br>
  - O primeiro a ser inserido é o primeiro a ser removido.
  <br>
  - A fila somente é acessível em duas posições:
  <br>
  &rarr; Início, para remoção.
  <br>
  &rarr; Fim, para inserção.
  <br>
  - Dessa forma as operações possiveis em uma fila são:
  <ul>
    <li> Enfileirar: inserir um elemento no fim da fila; </li>
    <li> Desenfileirar: remover e retornar o elemento inicial da fila; </li>
    <li> Vazia: verificar se a fila está vazia </li>
  </ul>
</p>
<img src = "https://user-images.githubusercontent.com/59178745/182468601-f3117fde-8493-41e8-a265-cbbec17a8319.png">
<h3> Utilização </h3>
<p>
  - Filas são utilizadas em situações em que há disputa por algum recurso.
  <br>
  Exemplo: processos disputando o uso do processador.
  <br>
  Variação: Fila com prioridades
  <br>
  - Em qualquer fila, a remoção de um elemento (e seu consequente acesso ao recurso disputado) ocorre na primeira posição.
  <br>
  - Entretando, pode-se considerar que os elementos possuem diferentes prioridade de acesso aos recursos.
  <br>
  - Isso deve ser levado em conta ao se fazer o escalonamento.
  <br>
  &rarr; Ou seja, os elementos podem ser inseridos na fila em posições que não sejam a última.
  <br>
  Exemplo: Uma fila em que idosos e gestantes tem prioridade. Neste caso, um idoso deve ser inserido na frente dos demais clientes, mas atrás de outros idosos ou gestantes.
</p>
