## CS32 Act II, Scene I -- Programming Assignment

*NOTE: The "PSet #4" assignment page on the CS 32 Canvas
site indicates when this assignment is due, what materials
you should submit, and how to submit them.*

**Goal:** Write a script that plays _SIX DEGREES OF KEVIN BACON_

**Introduction** In class, we learned how we can set up a search problem to discover a route from one real-world location to another using a network of roadways. We can use the same approach to solve any problem where we want to find a path between two states that we believe are connected by a sequence of transitions.

For example, you might use it to find whether there exists a sequence of known chemical reactions that allow you to change one compound into another. As another example, people often use goal-directed search in gameplay to find a sequence of moves that will lead their player to a winning state. We ourselves use goal-directed search when we pack a box with our stuff in order to move from school back to home. And biomedical researchers use goal-directed search when they attempt to find a sequence of amino acids that create a protein with the properties they need in treating some disease.

We’re going to use goal-directed search to determine whether two individuals are connected, as in the trivia game _Six degrees of Kevin Bacon_. The goal is to see if you can start with a movie star and then through a sequence of actors connect this star to another actor. The only rule is that the adjacent movie stars in the sequence you build must have starred together in a movie.

For example (borrowed from the Wikipedia page), if we wanted to know if Elvis Presley is connected to Kevin Bacon in this way, we might answer: Elvis Presley starred in the movie _Change of Habit_ (1969) with Edward Asner, and Asner was in _JFK_ (1991) with Kevin Bacon. 

Of course, not every movie star can be connected to another, but you’ve probably heard of the assertion that any two people on Earth are six or fewer acquaintances apart (probably fewer if you are allowed to use Facebook friends or LinkedIn connections).

**Your assignment:** In this pset, you will use a portion of the IMDb datasets about movies and movie actors to write a script that attempts to find a path from one movie star to another. A user of your script will specify the start and goal actors.

Your script should produce something like the following:

```
> python3 degrees32.py
Name: Demi Moore
Name: Dustin Hoffman
2 degrees of separation.
1: Demi Moore and Tom Cruise starred in A Few Good Men
2: Tom Cruise and Dustin Hoffman starred in Rain Man
```

In particular, it prompts the user for two names and then prints the number of degrees of separation and the path it found from the first actor to the second, or "not connected" if it cannot find a path.

**Step 1: Understanding the input IMDb files.** You will find three Comma-Separated Values (CSV) files in the directories in this project.

*   `movies.csv` associates a `movie_id` with a movie title and its release date.
*   `people.csv` associates a `person_id` with an actor's name and birth date (when known).
*   `stars.csv` links an actor's `person_id` with a movie's `movie_id` when that actor starred in that movie.

You will find a `small` directory, which contains these three files with just a few entries in them. We recommend developing your script using the files in this directory. You should use the `large` directory when you're confident that your script works.

Go ahead an open the three files under the `small` directory. CSV files are simply text files that you can easily read into a spreadsheet program. Each file line is a separate record, and the first line tells you the name given to each field in a record.

Lots of data on the internet is stored in CSV files, and so Python contains a library called `csv` that makes it easy to read and write CSV files. The first step in this pset is to learn a bit about this library and use it to build some Python dictionaries that you'll need to complete the pset.

**Open** the `step1.py` script. In it, you'll find a `main` routine that calls `load_data` and then runs a few tests on the data structures that `load_data` creates. This routine and its associated data structures are contained in the `degrees32_lib.py` file, and `step1.py` imports them for its use. You don't have to write any code in `step1.py`, but you should read it and make sure you understand how it works.

**You have to write code** in the routine `load_data` in `degree32_lib.py`. We have deleted the code you need to read in the file `movies.csv` and use its data to initialize the Python dictionary `movies`. From skimming the CSV library interface, reading the other code in `load_data` and the test code in `step1.py`, you should be able to figure out what code you need to write.

**Step 2: Get user input.** In this step, we want to grab the names of two actors and turn them into IMDb person identifiers. Again, we have placed the routine `get_person_id` that accomplishes most of this work in `degrees32_lib.py`, and the `main` routine in script `step2.py` calls it twice as a test.

You know how to be careful with user input from previous psets, and the interesting new aspect here is that we may have to ask the user to help us disambiguate between two actors with the same names. In other words, they've correctly typed an actor's name, but the IMDb files contain several actors with that name, but different ids. This work is done in `get_person_id`, and we've given you a complete, working routine.

**You have to write** the helper routine `build_names`. To allow you to test your code, the `main` routine in `step2.py` calls `build_names` and runs a small test on the the Python dictionary `names`.

When you get the code working, every actor in the `small` directory should have a single id except for "Emma Watson". If you input her name during the "TEST 4" testing code, the script should ask you to disambiguate between the two ids with this name.

**Step 3: A DFS for a path.** You are now set to write the full goal-directed search.  For this step, you'll use `degrees32.py`. In its `main` routine, you'll find that it calls `load_data` and then `get_person_id`. The actor who starts our search has its id loaded into `start` and the actor who ends our search has its id loaded into `goal`.

The `main` routine then calls `find_path`, which is **what you have to write**. 

The `path` returned from `find_path` is then printed out by the code at the end of `main`. You shouldn't have to change that code, if you create the path correctly.

We've done a few things to help you get started:

*   You'll find two classes in `degree32_lib.py` that you can use to implement the kind of node and frontier data structures we used in the driving-directions search problem we did together in class.  You shouldn't have to add any code to these data structures or their implementations
*   The beginning of `find_path` implements a sanity check that verifies the routine was given two different actors, and it initializes the `frontier` object you'll use. You simply need to create the initial `Node` object and loop that works on the objects it finds in the `frontier` until it encounters the goal state or runs out of objects in the `frontier` to process.
*   Remember that you can return as soon as you find the goal state (i.e., you don't have to put it into the `frontier` if you're script checks as you're putting objects onto the `frontier`).
*   Also remember that you should use the `"visited"` key in the dictionaries stored as values in the `people` dictionary to keep track of which states you have already visited.

**Step 4: A BFS for a path.** Congratulations on finding a path from one actor to another! As the last step in this pset, you will now find the **shortest path** from one actor to another, so that you can always win _Six Degrees of Kevin Bacon_ when you play it.

At the start of `find_path` in `degrees32.py`, you will remember seeing two commented-out lines below the lines that initialized the `frontier`.  Make those five lines look like the following:

```python
    # Initialize frontier
    # algo = 'dfs'
    # frontier = StackFrontier()
    algo = 'bfs'
    frontier = QueueFrontier()
```

Awesome. Now you need to implement the `class QueueFrontier`. Don't worry; it's not hard. It inherits all its methods and data attributes from `class StackFrontier` except one, which it overrides.

**You have to write** the following:

1.   Add `QueueFrontier` to the end of the `import` at the top of `degrees32.py`.
2.   Add `Class QueueFrontier` to the end of `degrees32_lib.py`. Don't forget to specify from which class it is derived.
3.   Figure out which class method you need to override to make a stack act like a queue.
4.   Write that method using the `Maze` and `CitySqGrid` classes from class as a template.

That's it!