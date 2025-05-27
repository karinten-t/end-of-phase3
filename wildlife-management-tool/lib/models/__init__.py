from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///wildlife.db')
Session = sessionmaker(bind=engine)
session = Session()


animal_habitat = Table(
    'animal_habitats',
    Base.metadata,
    Column('animal_id', Integer, ForeignKey('animals.id')),
    Column('habitat_id', Integer, ForeignKey('habitats.id'))
)

class Conservationist(Base):
    __tablename__ = 'conservationists'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    animals = relationship('Animal', backref='conservationist')

class Animal(Base):
    __tablename__ = 'animals'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    conservation_status = Column(String)
    conservationist_id = Column(Integer, ForeignKey('conservationists.id'))
    habitats = relationship('Habitat', secondary=animal_habitat, back_populates='animals')

class Habitat(Base):
    __tablename__ = 'habitats'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    habitat_type = Column(String)
    animals = relationship('Animal', secondary=animal_habitat, back_populates='habitats')

Base.metadata.create_all(engine)