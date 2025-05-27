from models import session
from helper import *

def debug():
  
    print("All Conservationists:")
    print(get_all_conservationists())
    
    print("\nAll Animals:")
    print(get_all_animals())

if __name__ == '__main__':
    debug()