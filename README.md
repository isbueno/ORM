# ORM

**Trabalho de Mapeamento Objeto-Relacional da disciplina de Laboratório de Banco de Dados**


Baseado no projeto de TCC Banco de Dados Genético para a substituição de animais em laboratórios.
</br></br>

## Resumo

Muito se discute a respeito dos testes feitos em animais e de toda a crueldade que existe neste processo. Para solucionar este problema são criados meios alternativos para realizar os experimentos. Com isso, o objetivo da criação do  Banco de Dados Genético é substituir os testes feitos em animais nos laboratórios de empresas a fim de testar produtos compatíveis com o corpo humano. Contendo informações sobre a sequência do DNA humano e das fórmulas dos produtos, será possível fazer comparações usando inteligência artificial para descobrir se as reações serão positivas ou negativas. Dessa maneira, os testes não envolvem o uso de animais, resultando na economia de tempo e recursos financeiros que seriam dedicados à cobaia.



</br></br>
## User Story 1
### Persona: Químico

"Eu como Químico responsável pelos testes, preciso de uma funcionalidade de cadastrar novos DNAs porque desejo inserir dados na minha tabela."

~~~
CA
Entregar sistema com função de inserir
Quando for possível cadastrar um novo DNA junto de ID, Nome, Sequência Genética, Proprietário.
Então será possível cadastrar um DNA.


DoD

![image](https://user-images.githubusercontent.com/102770607/193482184-e067002a-13ae-4652-9e5d-bef150510843.png)
Figura 1 - Menu de Operações para Adição dos dados

![image](https://user-images.githubusercontent.com/102770607/193482204-9ee92566-9f89-45d7-975e-be05430aac4a.png)
Figura 2 - Dados do "individuo 3" inseridos na tabela.

~~~

</br>

## User Story 2
### Persona: Químico

"Eu como Químico responsável pelos testes, preciso de uma funcionalidade de alterar atributos do DNAs porque podem ocorrer erros na inclusão."

~~~
CA
Entregar o sistema com a função de alterar dados
Quando for possível mudar qualquer um dos seus atributos em determinado DNA,
Então será possível alterar os atibutos na tabela. 


DoD
- Os dados de teste puderam ser alterados como é possível ver nas seguintes imagens: 

![image](https://user-images.githubusercontent.com/102770607/193481889-a6a847eb-eaa6-45fc-98f4-5c3612a23f07.png)
Figura 3 - Dados inseridos na tabela.

![image](https://user-images.githubusercontent.com/102770607/193481956-9ad19224-4d37-4681-9afb-114c8d07b19a.png)
Figura 4 - Menu de Operações para alteração dos dados


![image](https://user-images.githubusercontent.com/102770607/193481935-7bf53ff9-cf67-485e-bc17-94b8e8b2974e.png)
Figura 5 - Linha 2 "ATCAGTCATTACTACCTCTCTAGCT" foi alterado para "TTTTAAAAGGGGCCCC".
~~~

</br>

## User Story 3
### Persona: Químico

"Eu como Químico responsável pelos testes, preciso de uma funcionalidade de visualizar uma tabela específica de DNA para que facilite meu gerenciamento e testes."

~~~
CA
Entregar a funcionaliadde de exibir tabela do DNA
Quando for possível apresentar uma tabela com os dados de ID, Nome, Sequência Genética, Proprietário.
Então será possível visualizar a tabela.

DoD
- A tarefa pôde ser concluida como mostram as imagens abaixo:

![image](https://user-images.githubusercontent.com/102770607/193482006-33b079d7-d052-4076-8742-b76f843daad3.png)
Figura 6 - Menu de Operações para visualização dos dados e resultado da visualização.

![image](https://user-images.githubusercontent.com/102770607/193482114-4cfea966-880c-4d8e-a387-92ef2908b6e9.png)
Figura 7 - Visualização pelo terminal PowerShell para comparação.

~~~

</br></br>




## Relacionamentos
</br></br>
#### 1 RELACIONAMENTO 1:1

##### DNA x INDIVÍDUO </br>

Cada indivíduo só pode ter um DNA e um DNA só pode pertencer a um indivíduo. 


</br></br>
#### 2 RELACIONAMENTOS n:n

##### DNA x CATEGORIA </br>

Cada DNA pode ter mais de uma funcionalidade e uma funcionalidade pode ser agregada para mais de um DNA.
Isso foi quebrado em dois outros relacionamentos de 1:n (DNA x USO e Funcionalidade X USO)

##### DNA x Fórmula </br>

Um DNA pode ser testado em várias fórmulas e várias fórmulas podem ser testadas em um DNA.
Isso foi quebrado em dois relacionamentos de 1:n (DNA x Teste e Teste x Fórmula)


</br></br>
#### 3 RELACIONAMENTOS 1:n

##### DNA x Funcionalidade </br>

Esse relacionamento indica quais categorias serão agregadas para o DNA.

##### CATEGORIA x Funcionalidade </br>

Esse relacionamento vai indicar quais DNAs poderão ser usados para uma determinada categoria. 

##### COMBINAÇÂO x DNA </br>

A classe teste vai servir como um intermediário para o relacionamento de 1 DNA ser testado por várias fórmulas.

##### COMBINAÇÃO x Fórmula </br>

Aqui a classe teste tem a função contrária, servir de intermediário para o relacionamento em que 1 Fórmula é testada por diversos DNAs.

##### Marca x Fórmula </br>

Uma Marca pode disponibilizar diversas fórmulas para testes, enquanto uma fórmula só pertence a uma Marca.

##### Marca X Contato </br>

Uma Marca pode ter mais de um tipo de contato cadastrado no Banco de Dados, enquanto um contato só pode pertencer a uma Marca.


----


O código das três funcionalidades propostas nas User Storys pode ser conferido em "ORM.py"

Segue abaixo os Diagramas utilizados para a sua construção. Apesar de estarem mais completos do que o código, ele representa a relação principal proposta nesse diretório: a construção da relação INDIVÍDUO X DNA e suas funcionalidades (Alterar Sequencia Genética, Visualizar DNA e Inserir DNA).



![image](https://user-images.githubusercontent.com/102770607/193482961-d2e04659-88e6-45ce-b85e-515e5396d6e1.png)

Figura 8 - Modelo Relacional.

![image](https://user-images.githubusercontent.com/102770607/193482925-c3f09ef8-e5ae-4614-862c-3bc90b5bed07.png)

Figura 9 - Diagrama de Classe.
