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
(inserir)
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
(inserir)
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
(inserir)
~~~

</br></br>




## Relacionamentos
</br></br>
#### 1 RELACIONAMENTO 1:1

##### DNA x Proprietário </br>

Cada Proptrietário só pode ter um DNA e um DNA só pode pertencer a um indivíduo. 


</br></br>
#### 2 RELACIONAMENTOS n:n

##### DNA x Funcionalidade </br>

Cada DNA pode ter mais de uma funcionalidade e uma funcionalidade pode ser agregada para mais de um DNA.
Isso foi quebrado em dois outros relacionamentos de 1:n (DNA x USO e Funcionalidade X USO)

##### DNA x Fórmula </br>

Um DNA pode ser testado em várias fórmulas e várias fórmulas podem ser testadas em um DNA.
Isso foi quebrado em dois relacionamentos de 1:n (DNA x Teste e Teste x Fórmula)


</br></br>
#### 3 RELACIONAMENTOS 1:n

##### DNA x USO </br>

Esse relacionamento indica quais categorias (funcionalidades) serão agregadas para o DNA.

##### USO x Funcionalidade </br>

Esse relacionamento vai indicar quais DNAs poderão ser usados para uma determinada funcionalidade. 

##### Teste x DNA </br>

A classe teste vai servir como um intermediário para o relacionamento de 1 DNA ser testado por várias fórmulas.

##### Teste x Fórmula </br>

Aqui a classe teste tem a função contrária, servir de intermediário para o relacionamento em que 1 Fórmula é testada por diversos DNAs.

##### Marca x Fórmula </br>

Uma Marca pode disponibilizar diversas fórmulas para testes, enquanto uma fórmula só pertence a uma Marca.

##### Marca X Contato </br>

Uma Marca pode ter mais de um tipo de contato cadastrado no Banco de Dados, enquanto um contato só pode pertencer a uma Marca.
