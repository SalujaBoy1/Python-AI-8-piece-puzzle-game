The 8-puzzle problem is played on a 3-by-3 grid with 8 square tiles labeled 1 through 8 and a
blank tile. Your goal is to rearrange the blocks so that they are in order. You are permitted
to slide blocks horizontally or vertically into the blank tile.
In this project, I programmed a solution for the 8 piece puzzle game using 4 algorithms. 
These algorithms included Breadth-first search,  Iterative deepening search, and A* search using two different suitable heuristics. The heuristics used were the manhattan distance and misplaced tiles methods.

To run the program, use the terminal and include the algorithm arguement and the puzzle argument. 
The algorithm argument will be bfs, ids, astar1, or astar2. Finally the puzzle argument includes the tiles seoerated by spaces.
Here is an example:

python puzzlegame.py bfs "*" 1 3 4 2 5 7 8 6
python puzzlegame.py ids "*" 1 3 4 2 5 7 8 6
python puzzlegame.py astar1 "*" 1 3 4 2 5 7 8 6
python puzzlegame.py astar2 "*" 1 3 4 2 5 7 8 6
