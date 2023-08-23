# Questões de Pesquisa:
## RQ 01. Sistemas populares são maduros/antigos?

Métrica: idade do repositório (calculado a partir da data de sua criação)

## RQ 02. Sistemas populares recebem muita contribuição externa?

Métrica: total de pull requests aceitas

## RQ 03. Sistemas populares lançam releases com frequência?

Métrica: total de releases

## RQ 04. Sistemas populares são atualizados com frequência?

Métrica: tempo até a última atualização (calculado a partir da data de última atualização)

## RQ 05. Sistemas populares são escritos nas linguagens mais populares linguagens mais populares [octoverse search](https://octoverse.github.com/)?

Métrica: linguagem primária de cada um desses repositórios

## RQ 06. Sistemas populares possuem um alto percentual de issues fechadas?

Métrica: razão entre número de issues fechadas pelo total de issues

## Relatório Final:
- Para cada uma questões de pesquisa anteriores, faça uma sumarização dos dados obtidos através de valores medianos Links to an external site. 
- Mesmo que de forma informal, elabore hipóteses sobre o que você espera de resposta e tente analisar a partir dos valores obtidos. 
- Para valores de categoria (ex.: linguagem de programação), elabore uma contagem por categoria, para facilitar suas descobertas. 
- Elabore um documento que apresente (i) uma introdução simples com hipóteses informais; (ii) a metodologia que você utilizou para responder às questões de pesquisa; (iii) os resultados obtidos para cada uma delas; (iv) a discussão sobre o que você esperava como resultado (suas hipóteses) e os valores obtidos.  

### Bônus (+ 1 ponto):
Divida os resultados obtidos nas RQs 02, 03 e 04 por linguagem e analise como esses valores se comportam de acordo com as linguagem de cada repositório. Ou seja, acrescente ao seu trabalho a seguinte questão:

#### RQ. 07: Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?
Dica: compare os resultados para os sistemas com as linguagens da reportagem com os resultados de sistemas em outras linguagens.

### Processo de Desenvolvimento:
- Lab01S01: Consulta graphql para 100 repositórios (com todos os dados/métricas necessários para responder as RQs) + requisição automática (3 pontos)

- Lab01S02 (3 pontos):  
  - paginação (consulta 1000 repositórios)
  - dados em arquivo .csv 
  - primeira versão do relatório, com definição das hipóteses informais

- Lab01S03 (9 pontos): 
  - análise e visualização de dados + elaboração do relatório final

> Prazo final: 30/08 | Valor total: 15 pontos | Observação: NÃO é permitido o uso de bibliotecas de terceiros que realizem consultas à API do GitHub. É necessário que o aluno escreva a query GraphQL e faça o consumo da mesma a partir de um script próprio.