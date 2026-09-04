We will build an Engine at the end of this section:

Input:
    courses
    rooms
    times
    constraints

Output:
    schedule


The most important difference with Project 01

Project 01:
    Search in paths

Project 02:
    Search in the space of allocations

But the tool is common:
    State
    Search
    Heuristic
    Pruning (Removing parts of the search space that we know can no longer lead to a better or more valid answer.)