from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, update, engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.sql.expression import bindparam

URL = "mysql+mysqlconnector://root:password@localhost:3306/DBG"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin

Base = declarative_base()


class DNA(Base):
    __tablename__ = "DNA"
    id_dna = Column(Integer, primary_key=True)
    nomeDna = Column(String(150), nullable=False)
    sequenciaDna = Column(String(100), nullable=False)

    id_individuo = Column(Integer, ForeignKey("Individuo.id_individuo"))

    def __str__(self):
        return "DNA-----------------------\nid_dna: {} \nnome: {} \nsequencia: {})".format(
            self.id_dna, self.nomeDna, self.sequenciaDna
        )


class Individuo(Base):
    __tablename__ = "Individuo"
    id_individuo = Column(Integer, primary_key=True)
    nomeIndividuo = Column(String(150), nullable=False)
    idadeIndividuo = Column(Integer, nullable=False)
    sexoIndividuo = Column(String(1), nullable=False)

    contatos = relationship("Contato", backref="individuo")

    def __str__(self):
        return "Indivíduo(id_individuo = {}, nome = {}, idade = {}, sexo = {})".format(
            self.id_individuo, self.nomeIndividuo, self.idadeIndividuo, self.sexoIndividuo)


class Contato(Base):
    __tablename__ = "Contato"
    id_contato = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=False)
    numero = Column(String(20))

    id_individuo = Column(Integer, ForeignKey("Individuo.id_individuo"))

    def __str__(self):
        return "Contato(id_contato = {}, email = {}, numero = {})".format(
            self.id_contato, self.email, self.numero
        )


def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        individuo = Individuo(nomeIndividuo="Isabely", idadeIndividuo="19", sexoIndividuo="F")

        #        for i in range(10):
        individuo.contatos.append(
            Contato(email="23.isabelybueno@gmail.com", numero="+551299999999"))

        session.add(individuo)

    with Session.begin() as session:
        print("============================================")

        individuo = session.query(Individuo).get(1)

        print(individuo)

        for contato in individuo.contatos:
            print("   * " + str(contato))

    with Session.begin() as session:
        print("\n============================================")

        contato = session.query(Contato).get(5)

        print(contato)


if __name__ == "__main__":
    main()
