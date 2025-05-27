import inquirer
from helper import *

def main_menu():
    while True:
        questions = [
            inquirer.List('choice',
                message="Wildlife Management Tool - Main Menu",
                choices=[
                    'Add Conservationist',
                    'Add Animal',
                    'View Conservationists',
                    'View Animals',
                    'Add Habitat',
                    'Exit'
                ])
        ]
        answer = inquirer.prompt(questions)
        
        if answer['choice'] == 'Add Conservationist':
            name = input("Enter conservationist name: ")
            email = input("Enter email: ")
            create_conservationist(name, email)
            print("Conservationist added!")
        
        elif answer['choice'] == 'Add Animal':
            name = input("Animal name: ")
            species = input("Species: ")
            status = input("Conservation status: ")
            cons_id = input("Conservationist ID: ")
            create_animal(name, species, status, cons_id)
            print("Animal added!")
        
        elif answer['choice'] == 'View Conservationists':
            cons = get_all_conservationists()
            for c in cons:
                print(f"{c.id}: {c.name} - {c.email}")
        
        elif answer['choice'] == 'Exit':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main_menu()