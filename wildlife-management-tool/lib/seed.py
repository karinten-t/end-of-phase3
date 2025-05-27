from faker import Faker
from helper import *
from models import session

fake = Faker()

def seed_database():
    # Create conservationists
    for _ in range(5):
        create_conservationist(fake.name(), fake.email())
    
    # Create habitats
    habitats = ['Rainforest', 'Savanna', 'Coral Reef', 'Wetland']
    for habitat in habitats:
        create_habitat(habitat, fake.word())
    
    
    species = ['Tiger', 'Elephant', 'Panda', 'Sea Turtle']
    statuses = ['Endangered', 'Critically Endangered', 'Vulnerable']
    conservationists = get_all_conservationists()
    
    for _ in range(20):
        create_animal(
            name=fake.first_name(),
            species=fake.random.choice(species),
            status=fake.random.choice(statuses),
            conservationist_id=fake.random.choice(conservationists).id
        )
    
    
    animals = get_all_animals()
    habitats = session.query(Habitat).all()
    
    for animal in animals:
        add_animal_to_habitat(animal.id, fake.random.choice(habitats).id)

if __name__ == '__main__':
    seed_database()