<h1> Balanceamento em Árvores Binárias </h1>
<p>
  - Uma <abbr title = "Binary Search Tree"> BST</abbr> é uma forma de localizar uma informação, sem ter que verificar cada um dos elementos.
  <br>
  - Entretanto, para que a busca seja vantajosa, é preciso que a distribuição dos elementos esteja equilibrada. (<em>Balanceamento</em>)
  <br>
  - Uma árvore é dita balanceada se, para todos os seus nós:
  <br>
  &rarr; A diferença de altura entre as sub-árvores da esquerda e da direita é, <strong> no máximo, igual a um. </strong> Exemplos:
</p>
<img>
<h2> Balanceamento Estático x Balanceamento Dinâmico </h2>
<p>
  - O Balanceamento Estático é feito em uma árvore construída de forma desbalanceada.
  <br>
  - Os elementos são salvos em uma estrutura auxiliar, a árvore é destruída e reconstruída de maneira balanceada. Ou seja:
  <ol>
    <li> Construir uma estrutura auxiliar com os elementos ordenados; </li>
    <li> Remover a árvore da memória; </li>
    <li> Refazer a árvore com os elementos da estrutura auxiliar. </li>
  </ol>
</p>
<h2> Balanceamento Dinâmico </h2>
<p>
  - O Balanceamento Dinâmico acontece à medida que inserções e remoções provocam o desbalanceamento da árvore.
  <br>
  - Algumas árvores que possuem Balanceamento Dinâmico:
  <ul>
    <li> Árvores AVL. </li>
    <li> Árvores Vermelho e Preto. </li>
  </ul>
</p>
