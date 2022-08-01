<h1> Recursividade </h1>
<p>
  Chamadas as funções, funcionam como um desvio de fluxo de código.
  <br>
  - O código da função fica salvo para ser executado no momento em que houver uma chamada.
  <br>
  Exemplo:
</p>
<pre>
  <code>
    def funcao_a():
      &rarr; código
    mais código...
    funcao_a() &larr; chamada
    mais código...
  </code>
</pre>
<p>
  Uma função pode chamar outra função.
  <br>
  Exemplo:
</p>
<pre>
  <code>
    def funcao_b():
      código
      funcao_a()
      mais código
  <code>
</pre>
<p>
  Uma função é dita recursiva quando dentro do seu corpo existe uma chamada a si própria. Assim:
</p>
<pre>
  <code>
    def funcao_rec():
      código
      &rarr; funcao_rec()
      mais código
  </code>
</pre>
<h2> Como Funciona? </h2>
<p>
  Como se fosse uma função qualquer sendo chamada, no momento da chamada existe um desvio de fluxo de execução; a função reinicia.
</p>
<h3> Mas isso não seria infinito? </h3>
<p>
  Se não tomar cuidado, sim! Ou melhor, infinito até esgotar toda a memória.
  <br>
  - <em> Overflow </em> (estouro de memória).
  <br>
  Para evitar, <strong> toda </strong> função recursiva deve possuir uma <strong> condição de parada</strong>.
  <br>
  É uma condição (if, while, etc) que impede a função de ser executada "para sempre", algo deve mudar de uma execução para outra.
  <br>
  - Parâmetros
  <br>
  Cada execução da função tem seu próprio espaço reservado na memória.
</p>
<h2> Elaborando Funções Recursivas </h2>
<p>
  Ao chamar uma função, nos comportamos como "clientes" dessa função. Nos preocupamois com <ins> o que</ins> será feito, não com o <ins> como</ins>.
  <br>
  <a href = "#"> Exemplo: Fatorial </a>
  <br>
  <a href = "#"> Exemplo: Fibonacci </a>
  <br>
  <a href = "#"> Exemplo: Imprimir Vetor </a> 
</p>
