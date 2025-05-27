from models import session, Conservationist, Animal, Habitat


def create_conservationist(name, email):
    conservationist = Conservationist(name=name, email=email)
    session.add(conservationist)
    session.commit()
    return conservationist

def get_all_conservationists():
    return session.query(Conservationist).all()

def find_conservationist_by_id(id):
    return session.query(Conservationist).filter(Conservationist.id == id).first()


def create_animal(name, species, status, conservationist_id):
    animal = Animal(
        name=name,
        species=species,
        conservation_status=status,
        conservationist_id=conservationist_id
    )
    session.add(animal)
    session.commit()
    return animal

def get_all_animals():
    return session.query(Animal).all()


def create_habitat(name, habitat_type):
    habitat = Habitat(name=name, habitat_type=habitat_type)
    session.add(habitat)
    session.commit()
    return habitat

def add_animal_to_habitat(animal_id, habitat_id):
    animal = session.query(Animal).get(animal_id)
    habitat = session.query(Habitat).get(habitat_id)
    habitat.animals.append(animal)
    session.commit()