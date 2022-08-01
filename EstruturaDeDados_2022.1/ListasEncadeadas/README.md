<h1> Listas Encadeadas </h1>
<h2> Tipo Abstrato de Dados (TAD) </h2>
<p>
  Um TAD é uma estrutura composta dos seguintes elementos:
  <br>
  &rarr; Definição de dados a serem armazenados;
  <br>
  &rarr; Definição de funções para manipulação destes dados.
  <br>
  Um TAD deve apenas ser manipulado através das funções definidas com este fim.
  <br>
  Isso permite que se crie Estrutura de Dados com restrições de acesso e manipulação, desenvolvidas com um fim específico.
  <br>
  Uma aplicação do conceito de TAD é o desenvolvimento de classes, onde:
  <br>
  &rarr; Atributos são os dados;
  <br>
  &rarr; Métodos são funções definidas para acesso aos dados.
  <br>
  O encapsulamento de atributos protege da operação indevida da estrutura. Por exemplo: Listas.
</p>
<h2> Listas Encadeadas </h2>
<p>
  Listas encadeadas são um TAD que simula a disposição sequencial dos elementos na memória.
  <br>
  &rarr; Os elementos não ficam necessariamente em sequência, mas a lista abstrai isso. Para tanto, cada elemento traz consigo uma referência para a posição de memória em que se encontra o próximo elemento.
</p>
<img src = "https://user-images.githubusercontent.com/59178745/182227578-e0f24f7b-8b33-4bea-b488-cc674923d9e6.png">
<p>
  Deve existir um apontador inicial (Head) a partir do qual se tem acesso a todo o conteúdo.
  A última posição, como não possui um próximo endereço para referenciar, deve apontar para <ins> lugar nenhum</ins>.
  <br>
  &rarr; Em Python: <em> None</em>.
  <br>
  A lista é um TAD de acesso livre.
  <br>
  Pode-se acessá-la e manipulá-la em qualquer posição. Isso possibilita o desenvolvimento de uma grande quantidade de funções para a sua manipulação.
  <ul>
    <li> <em> append</em>; </li>
    <li> <em> insert</em>; </li>
    <li> <em> pop</em>; </li>
    <li> <em> sort</em>; </li>
    <li> <em> invert</em>; </li>
    <li> <em> extend</em>; </li>
    <li> <em> len</em>; </li>
    <li> etc. </li>
  </ul>
</p>
<h2> Variações de Listas Encadeadas </h2>
<p>
  A lista representada é uma lista simplesmente encadeada pelo fato de existir apenas um encadeamento simples, para a posição seguinte.
  <br>
  Pode-se, para facilitar a manipulação e otimizar desempenho, usar um encadeamento duplo:
</p>
<img src = "https://user-images.githubusercontent.com/59178745/182227720-64e52e96-518d-4137-a1b3-4fec719c4fa5.png">
<p>
  Também pode-se utilizar uma estrutura adicional para referenciar o início e o fim da lista, por questão de desempenho:
</p>
<img>
