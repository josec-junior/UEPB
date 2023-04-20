<h1> Atividade 05 - Projeto </h1>
<p>
    Usando o script <a href = ""> script_ativ.sql</a> e usando o Postgresql, resolva os problemas a seguir:
</p>
<ol>
    <li>
        Crie uma função para reajustar salários. O reajuste deve ser aplicado para todos os funcionários, e deve seguir a seguinte tabela:
        <ul>
            <li> 5% de reajuste para os funcionários que não estão envolvidos em nenhuma atividade de projeto; </li>
            <li> 10% de reajuste para os funcionários que estão envolvidos em até 2 atividades de projeto; </li>
            <li> 15% de reajuste para os funcionários que estão envolvidos em pelo menos 3 atividades de projeto. </li>
        </ul>
    </li>
    <li>  Execute o reajuste criado na questão 1. </li>
    <li> Modifique a tabela Departamentos, acrescentando uma coluna chamada total_atividades (numeric). Essa coluna deve ser preenchida para todos os departamentos, contendo o número de atividades desenvolvidas, somando todos os projetos daquele departamento específico. </li>
    <li> Crie um gatilho na tabela AtividadesProjetos, para que cada vez que uma nova linha seja inserida a tabela Departamentos tenha o seu campo total_atividades ajustado no departamento responsável pelo projeto no qual foi realizada uma nova atividade. </li>
    <li> Crie uma tabela chamada Prêmios (id, funcionario_id, data, valor). </li>
    <li> Crie um gatilho na tabela AtividadesProjetos, para que cada vez que uma nova linha seja inserida, caso o funcionário responsável pelo projeto tenha atingido 3 atividades, receba um prêmio de 20% do salário (inserido na tabela prêmio). </li>
    <li> Crie uma visão chamada Total_premios_2022, que contenha o nome do funcionário e o total em prêmios que ele tem a receber em 2022. </li>
</ol>
