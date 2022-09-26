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

DNA x PRoprietário </br>

#### 2 Relacionamentos :n

DNA x Funcionalidade </br>
DNA x Fórmula </br>

#### 3 Relacionamento 1:n

Teste x DNA </br>
Teste x Fórmula </br>
Marca x Fórmula </br>
Marca X Contato </br>
