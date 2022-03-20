'''Driver routine for step 2'''

import sys
from degrees32_lib import load_data, build_names, get_person_id, names

def main():
    # Read CSV files into `people` and `movies` dictionaries
    load_data()

    # Build mapping from lower-cast names to person_ids
    build_names()

    # TEST3: What person_ids go with Tom Hanks and Emma Watson?
    print('\n## TEST 3 ##')
    print(f'Tom Hanks = {names["tom hanks"]}')
    print(f'Emma Watson = {names["emma watson"]}')

    # TEST4: Testing user-input routines
    print('\n## TEST 4 ##')
    start = get_person_id()
    if start == None:
        sys.exit('Person not found')
    goal = get_person_id()
    if goal == None:
        sys.exit('Person not found')
    print(f'Ready to find a path from {start} to {goal}!')

if __name__ == '__main__':
    main()