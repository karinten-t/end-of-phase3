# Wildlife Management Tool

A CLI application for managing endangered species and conservation efforts.
## project structure

wildlife-management-tool/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib/
    ├── __init__.py
    ├── models/
    │   ├── __init__.py
    ├── cli.py
    ├── debug.py
    ├── seed.py
    └── helper.py

## Setup
1. Install dependencies: `pipenv install`
2. Enter virtualenv: `pipenv shell`
3. Seed database: `python lib/seed.py`
4. Run application: `python lib/cli.py`

## Features
- Track conservationists and their assigned animals
- Manage animal habitats and conservation status
- View relationships between animals and habitats