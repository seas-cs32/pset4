'''Driver routine for step 1'''

from degrees32_lib import load_data, people, movies

def main():
    # Read CSV files into `people` and `movies` dictionaries
    load_data()
    
    # TEST1: Who is star with person_id = 158 and
    # what movies did he/she star in?
    print('\n## TEST 1 ##')
    person_id = 158
    name = people[person_id]["name"]
    print(f'Person_id {person_id} is {name}, who starred in:')
    for movie_id in people[person_id]["movies"]:
        print(f'  {movies[movie_id]["title"]} ({movies[movie_id]["year"]})')

    # TEST2: Who co-starred with person_id = 158 in movie_id = 112384?
    print('\n## TEST 2 ##')
    person_id = 158
    movie_id = 112384
    title = movies[movie_id]["title"]
    print(f'{name} co-starred in {title} with:')
    for costar_id in movies[movie_id]["stars"]:
        if costar_id != 158:
            print(people[costar_id]["name"])
        
if __name__ == '__main__':
    main()