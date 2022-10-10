from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, update, engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.sql.expression import bindparam

URL = "mysql+mysqlconnector://root:password@localhost:3306/DBG"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin

Base = declarative_base()


class Individuo(Base):
    __tablename__ = "Individuo"
    id_individuo = Column(Integer, primary_key=True)
    nomeIndividuo = Column(String(150), nullable=False)
    idadeIndividuo = Column(Integer, nullable=False)
    sexoIndividuo = Column(String(1), nullable=False)
    dnaR = relationship("DNA", back_populates="Individuo")


class DNA(Base):
    __tablename__ = "DNA"
    id_dna = Column(Integer, primary_key=True)
    nomeDna = Column(String(150), nullable=False)
    sequenciaDna = Column(String(100), nullable=False)
    id_individuo = Column(Integer, ForeignKey("Individuo.id_individuo"))
    # many-to-one scalar
    Individuo = relationship("Individuo", back_populates="dnaR")


engine = create_engine(url=URL)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(engine, expire_on_commit=False)


def addDna():
    with Session.begin() as session:
        print("DNA-------------")
        print("Nome: ")
        dna = DNA()
        dna.nomeDna = input()
        print("\nSEQUENCIA: ")
        dna.sequenciaDna = input()
        id_dna = dna.id_dna

        print("Individuo----------")
        individuo = Individuo()
        print("Nome: ")
        individuo.nomeIndividuo = input()
        print("Idade: ")
        individuo.idadeIndividuo = input()
        print("Sexo: ")
        individuo.sexoIndividuo = input()

        session.add(individuo)
        session.flush()
        session.add(dna)


def editDna():
    ATUAL = input("ATUAL: ")
    NOVO = input("NOVO: ")
    with engine.connect() as connection:
        connection.execute("UPDATE DNA SET sequenciaDna=\"" + NOVO + "\" WHERE nomeDna= \"" + ATUAL + "\"")
        print("Dados Atualizados com sucesso!")


def viewDna():
    nomeProcura = input("NOME: ")
    with engine.connect() as connection:
        result_set = connection.execute(" SELECT nomeDNA, sequenciaDna FROM DNA WHERE nomeDna=\""+ nomeProcura + "\"")
        print("-------------------------")
        for row in result_set:
            print("NOME: " + row[0] +"\nSEQUÊNCIA: " + row[1])


def menu():

    print("1 -  INSERIR DNA\n"
          "2 -  EDITAR DNA\n"
          "3 -  VISUALIZAR DNA\n\n")
    opcao = input("Selecione a opção desejada:")

    match opcao:
        case "1":
            addDna()

        case "2":
            editDna()

        case "3":
            viewDna()


def main():
    menu()


if __name__ == "__main__":
    main()
