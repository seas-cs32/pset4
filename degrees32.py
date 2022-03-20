'''Find a 6-degrees-of-Kevin-Bacon-like path from
one actor to another using IMBd data.'''

import sys
from degrees32_lib import load_data, people, movies, get_person_id, Node, StackFrontier

def find_path(start, goal):
    """
    Returns a list of (movie_id, person_id) pairs that
    connect the start person_id to the goal person_id.

    If no possible path, returns None.
    """

    # Sanity check input
    if start == goal:
        sys.exit("ERROR: You must input two DIFFERENT people!")

    # Initialize frontier
    algo = 'dfs'
    frontier = StackFrontier()
    # algo = 'bfs'
    # frontier = QueueFrontier()
    print(f'Running a {algo} search')

    ### ADD CODE HERE for STEP 3


def main():
    # Read CSV files into `people` and `movies` dictionaries
    load_data()

    # Grab start and goal actor names from user
    start = get_person_id()
    if start == None:
        sys.exit('Person not found')
    goal = get_person_id()
    if goal == None:
        sys.exit('Person not found')

    # Find a path from start to goal, if one exists
    path = find_path(start, goal)

    # Print degrees of separation and path for user
    if path is None:
        print("Not connected.")
    else:
        degrees = len(path) - 1
        print(f"{degrees} degrees of separation.")
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

if __name__ == '__main__':
    main()
