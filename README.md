# ORM

**Trabalho de Mapeamento Objeto-Relacional da disciplina de Laboratório de Banco de Dados**


Baseado no projeto de TCC Banco de Dados Genético para a substituição de animais em laboratórios
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
aqui tem meu definition of done
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
aqui tem meu definition of done
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
aqui tem meu definition of done
~~~

</br>


---

## Relacionamentos

#### 1 Relacionamento 1:1

##### DNA x Proprietário </br>

Cada Proptrietário só pode ter um DNA e um DNA só pode pertencer a um indivíduo 

#### 2 Relacionamentos n:n

##### DNA x Funcionalidade </br>

Cada DNA pode ter mais de uma funcionalidade e uma funcionalidade pode ser usada para mais de um DNA.
Isso foi quebrado em dois outros relacionamentos de 1:n (DNA x USO e Funcionalidade X USO)

##### DNA x Fórmula </br>

Um DNA pode ser testado em várias fórmulas e várias fórmulas podem ser testadas em um DNA.
Isso foi quebrado em dois relacionamentos 1:n (DNA x Teste e Teste x Fórmula)

#### 3 Relacionamento 1:n

##### DNA x USO </br>

Esse relacionamento indica para que o DNA pode ser utilizado, em quais categorias de funcionalidades ele se encaixa para teste.

##### USO x Funcionalidade </br>

Esse relacionamento vai indicar quais DNAs poderão ser usados para uma determinada funcionalidade. 

##### Teste x DNA </br>

A classe teste vai servir como um intermediário para o relacionamento de 1 DNA ser testado por várias fórmulas.

##### Teste x Fórmula </br>

Aqui a classe teste tem a função contrária, servir de intermediário para o o relacionamento de 1 Fórmula ser testada por diversos DNAs.

##### Marca x Fórmula </br>

Uma Marca pode disponibilizar diversas fórmulas para testes.

##### Marca X Contato </br>

Uma Marca pode ter mais de um tipo de contato cadastrado no Banco de Dados.
