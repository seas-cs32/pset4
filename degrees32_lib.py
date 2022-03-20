''' degrees32_lib contains several routines you will
complete on the way to completing degrees32.py'''

import csv

### Routines and data structures for steps 1-4

people = {}
movies = {}

def load_data(directory='small'):
    """
    Load data from CSV files into `people` and `movies` dictionaries
    """

    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            id = int(row["id"])
            people[id] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set(),
                "visited": False
            }

    # Load movies
    ### ADD CODE HERE for STEP 1

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            person_id = int(row["person_id"])
            movie_id = int(row["movie_id"])
            try:
                people[person_id]["movies"].add(movie_id)
                movies[movie_id]["stars"].add(person_id)
            except KeyError:
                pass

    # Client scripts should import people, movies
    return None


### Routines and data structures for steps 2-4

names = {}

def build_names():
    """
    Return a dictionary that maps a name to
    one or more person_ids.  The name key to
    this dictionary should contain only
    lower-case letter.
    """
    ### ADD CODE HERE for STEP 2

    # Clients may import names
    return None

def get_person_id():
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """

    # Verify that `names` dictionary has been initialized
    if len(names) == 0:
        build_names()

    # Grab an actor name from user
    name = input("Name: ")

    # Start process of disambiguation
    person_ids = list(names.get(name.lower(), set()))

    if len(person_ids) == 0:
        return None

    elif len(person_ids) > 1:
        print(f"Which '{name}'?")

        # List out potential people
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")

        person_id = int(input("Intended Person ID: "))
        if person_id in person_ids:
            return person_id
        return None

    else:
        return person_ids[0]


### Routines and data structures for steps 3 and 4

class Node():
    """
    Node holding state that indicates what action
    took us here from a previous state (parent)
    """
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

    def __str__(self):
        return f'n{self.state}'


class StackFrontier():
    """
    A frontier data structure implemented as a
    last-in first-out (LIFO) stack
    """
    def __init__(self):
        self.frontier = []

    def __str__(self):
        s = '['
        for elem in self.frontier:
            s += f'{elem},'
        return s + ']'

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
