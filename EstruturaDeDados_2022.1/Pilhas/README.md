<h1> Pilhas </h1>
<h2> Pilhas e Filas </h2>
<p>
  - São dois tipos abstratos de dados sequenciais;
  <br>
  - Se diferenciam de Listas, pois possuem restrições de acesso;
  <br>
  - Ou seja, <strong> nem toda operação é permitida </strong> em uma Pilha ou Fila.
</p>
<h2> Pilhas </h2>
<p>
  Estrutura LiFo - <em> Last in, First out </em>
  <br>
  - O último a ser inserido é o primeiro a ser removido.
  <br>
  - Em uma pilha, o acesso é permitido em uma única posição: o início da pilha ou o seu topo.
  <br>
  - Para manter a analogia, imaginemos uma pilha de elementos na vertical.
</p>
<img src = "https://user-images.githubusercontent.com/59178745/182507130-ee336665-c19a-436a-ae5c-c56598ff5108.png">
<h3> Operações </h3>
<ul>
  <li> <em> push</em>: Insere um elemento no topo da pilha; </li>
  <li> <em> pop</em>: Remove e retorna o elemento que está no topo da pilha; </li>
  <li> <em> isEmpty</em>: Verifica se a pilha está vazia. </li>
</ul>
<h3> Utilizações </h3>
<p>
  - Situações em que o último elemento deve ser priorizado incluem: Recursividade.
  <br>
  - A última chamada recursiva realizada é que deve assumir o controle e continuar a execução quando uma execução atinge a condição de parada.
  <br>
  &rarr; Inversão de uma sequência de elementos;
  <br>
  &rarr; Controle de paridade de elementos, por exemplo, parênteses em uma expressão.
</p>
