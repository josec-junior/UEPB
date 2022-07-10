<h1> Árvores Binárias </h1>
<p> - Em uma árvore binária, cada nó possui dois filhos, sendo um filho à esquerda e outro filho à direita. </p>
<p> - Será trabalhado especificamente com um tipo de árvore binária, a <em> Binary Seach Tree </em> (BST), ou Árvore Binária de Busca/Pesquisa.
<p> Em uma BST, (Considerando uma informação como sendo a chave da pesquisa), <ins> Todos os nós</ins> devem obdecer às seguintes regras:
<ul>
  <li> Todos os nós na sub-árvore <strong> à esquerda </strong> devem possuir chaves menores. </li>
  <li> Todos os nós na sub-árvore <strong> à direita </strong> devem possuir chaves maiores. </li>
</ul>
<p> Com essas regras (as quais permitem uma rápida localização), toda informação deve ocupar um lugar específico na árvore. </p>
<p> Por exemplo: Inserir numa BST, elementos com as chaves a seguir, respeitando a ordem: 20 → 13 → 7 → 42 → 25 → 3 → 18 → 37 → 22 → 10. Temos: </p>
<img src = "https://user-images.githubusercontent.com/59178745/178126599-eeac42aa-8d97-4f9f-b366-1f206b10fb3b.jpg">

<h2> Percorrimento em Árvores Binárias </h2>
<p> - Percorrer uma árvore binária é um procedimento que deve garantir: </p>
<ol>
  <li> A visitação de todos os elementos da árvore; </li>
  <li> O processamento de cada nó correndo uma única vez. </li>
</ol>
<p> - Há três maneiras de se percorrer uma árvore. </p>
<p> - Em todas elas, o elemento <strong> à esquerda </strong> será visitado antes do elemento <strong> à direita</strong>.
<p> - O que muda é o momento do <strong> processamento do nó </strong> em relação às visitas à esquerda e à direita.
<p>
  Percorrimento em:
  <br>
  <br>
  <strong> <ins> Pré-ordem </ins> </strong>
  <ol>
    <li> Processa o nó; </li>
    <li> Visita esquerda; </li>
    <li> Visita direita. </li>
  </ol>
  <strong> <ins> Ordem central </ins> </strong>
  <ol>
    <li> Visita esquerda; </li>
    <li> Processa o nó; </li>
    <li> Visita direita. </li>
  </ol>
  <strong> <ins> Pós-ordem </ins> </strong>
  <ol>
    <li> Visita esquerda; </li>
    <li> Visita direita; </li>
    <li> Processa o nó. </li>
  </ol>
</p>
<p>
  Exemplo:
  <br>
  <img src = "https://user-images.githubusercontent.com/59178745/178144695-b231c7d9-1b72-4fec-b835-6315920a33f4.png">
</p>
<p>
  <strong> <ins> Pré-ordem</ins> </strong>: 20 → 13 → 7 → 3 → 10 → 18 → 42 → 25 → 22 → 37
  <br>
  <strong> <ins> Ordem central</ins> </strong>: 3 → 7 → 10 → 13 → 18 → 20 → 22 → 25 → 37 → 42
  <br>
  <strong> <ins> Pós-ordem</ins> </strong>: 3 → 10 → 7 → 18 → 13 → 22 → 37 → 25 → 42 → 20
</p>
