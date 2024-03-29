<h1> Grafos </h1>
<p>
  - Estrutura que representa o relacionamento entre as informações.
  <br>
  - Um grafo é constituído por dois conjuntos:
  <br>
  &rarr; Vértices
  <br>
  &rarr; Arestas
  <br>
  - Um vértice representa um elemento, enquanto uma aresta representa a relação entre dois elementos.
  <br>
  Exemplo:
</p>
<img src = "https://user-images.githubusercontent.com/59178745/183762492-44b03129-294c-4ac5-9df9-8527ca4c4f01.png">
<p>
  Vértices: <em> V = {A, B, C, D} </em>
  <br>
  Arestas: <em> A = {(A, B), (A, C), (B,D), (C,D)} </em>
</p>
<h2> Aplicações </h2>
<ul>
  <li> Mapas Rodoviários </li>
  <li> Redes Sociais </li>
  <li> Etapas de um Projeto </li>
  <li> Etc. </li>
</ul>
<h2> Formas de Representação </h2>
<ol>
  <li> Estrutura de Adjacência </li>
  <li> Matriz de Adjacência </li>
</ol>
<h3> Estrutura de Adjacência </h3>
<img src = "https://user-images.githubusercontent.com/59178745/183540866-b4440647-0823-4bfb-8ca4-68e5bd3f81f0.png">
<h3> Matriz de Adjacência </h3>
<p>
  - Matriz de N x N elementos, onde N = número de vértices;
  <br>
  - Cada posição representa a existência ou não de uma adjacência entre os vértices representados na linha e na coluna.
</p>
<img src = "https://user-images.githubusercontent.com/59178745/183540904-4cbb77f1-e099-474b-97fe-1a3fead921c3.png">
<h2> Percorrimento </h2>
<ol>
  <li> Amplitude </li>
  <li> Profundidade </li>
</ol>
<h3> Amplitude </h3>
<p>
  - A partir de um vértice, percorre-se imediatamente todos os seus adjacentes.
  <br>
  - Cada vértice percorrido é colocado em uma Fila (<abbr title = "First In, First Out">FIFO</abbr>), para organizar o próximo vértice a ter seus adjacentes percorridos.
  <br>
  - Cada vértice visitado é marcado como tal, para não ser visitado novamente.
</p>
<h3> Profundidade </h3>
<p>
  - Ao se visitar um vértice, imediatamente visita-se um de seus adjacentes, a partir do qual repete-se o procedimento, até que não haja novos adjacentes.
  <br>
  Então, faz-se o caminho de volta, buscando-se outros adjacentes não visitados.
</p>
<img src = "https://user-images.githubusercontent.com/59178745/184558954-b660cb0c-31c6-41cf-8101-d8236377c03e.png">
