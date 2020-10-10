import sys
from collections import deque

SolutionState = ["1","2","3","4","5","6","7","8","*"]

class Node:
  def __init__(self, state=None, depth=0, parent=None):
    self.state = state
    self.up = None
    self.down = None
    self.left = None
    self.right = None
    self.depth = depth
    self.parent = parent
    self.g = 0.0
    self.h = 0.0
    self.f = (.5 * self.g) + (.5 * self.h)
    self.isSolution = (self.state == SolutionState)
    self.empty_index = state.index("*")


def print_board_state(state):
  line_count = 0
  for cell in state:
    if line_count < 2:
      print(cell, end=" ")
      line_count = line_count + 1
    else:
      print(cell)
      line_count = 0
  print(" \n")

def bfs(root):
    if root is None: 
        return
    queue = deque()
    queue.append(root)
    queue_count = 0
    while(len(queue) > 0):
      node = queue.popleft()
      queue_count = queue_count + 1

      if node.isSolution:
        return node, queue_count

      if(node.left is not None):
        queue.append(node.left)
      if(node.right is not None):
        queue.append(node.right)
      if(node.down is not None):
        queue.append(node.down)
      if(node.up is not None):
        queue.append(node.up)

def dls(root, max_depth, count):
  count = count + 1
  if root != None and root.isSolution:
      return True, root, count

  if max_depth == 0:
    return False, None , count

  if(root.left is not None):
    found, solution, count = dls(root.left, max_depth - 1, count)
    if found:
      return True, solution, count
  if(root.right is not None):
    found, solution, count = dls(root.right, max_depth - 1, count)
    if found:
      return True, solution, count
  if(root.down is not None):
    found, solution, count = dls(root.down, max_depth - 1, count)
    if found:
      return True, solution, count
  if(root.up is not None):
    found, solution, count = dls(root.up, max_depth - 1, count)
    if found:
      return True, solution, count

  return False, None, count

def IDS(root):
  count = 0
  for i in range(0,9):
    found, solution, count = dls(root, i, count)
    if found:
      return solution, count
  return None, count

def heuristic1(state):
  count = 8
  for i in range(9):
    if state[i] == "*":
      if(i == 8):
        count = count - 1
    elif int(state[i]) == (i + 1):
        count = count - 1

  return count

def a_star1(root):
  open = []
  closed = []
  count = 0

  open.append(root)
  while len(open) > 0:
    min_node = open[0]
    for node in open:
      if(node.f < min_node.f):
        min_node = node  
    
    count = count + 1

    if min_node.isSolution:
      return min_node, count

    open.remove(min_node)
    child = None
    if(min_node.left is not None):
      child = min_node.left
      current_cost = min_node.g  + 1
      if(child in open):
        if child.g <= current_cost:
          continue
      elif child in closed:
        if child.g <= current_cost:
          continue
        closed.remove(child)
        open.append(child)
      else:
        open.append(child)
        child.h = heuristic1(child.state)
      child.g = current_cost

    if(min_node.right is not None):
      child = min_node.right
      current_cost = min_node.g + 1 
      if(child in open):
        if child.g <= current_cost:
          continue
      elif child in closed:
        if child.g <= current_cost:
          continue
        closed.remove(child)
        open.append(child)
      else:
        open.append(child)
        child.h = heuristic1(child.state)
        child.g = current_cost

    if(min_node.down is not None):
      child = min_node.down
      current_cost = min_node.g + 1
      if(child in open):
        if child.g <= current_cost:
          continue
      elif child in closed:
        if child.g <= current_cost:
          continue
        closed.remove(child)
        open.append(child)
      else:
        open.append(child)
        child.h = heuristic1(child.state)
      child.g = current_cost
    
    if(min_node.up is not None):
      child = min_node.up
      current_cost = min_node.g + 1
      if(child in open):
        if child.g <= current_cost:
          continue
      elif child in closed:
        if child.g <= current_cost:
          continue
        closed.remove(child)
        open.append(child)
      else:
        open.append(child)
        child.h = heuristic1(child.state)

      child.g = current_cost

    closed.append(min_node)
  return None, count

def heuristic2(state):
  sum = 0
  for i, val in enumerate(state):
    if val != "*":
      sum = sum + (abs((int(val)-1)%3 - i%3) + abs((int(val)-1)//3 - i//3))
  return sum 

def a_star2(root):
  open = []
  closed = []

  open.append(root)
  count = 0
  while len(open) > 0:
    min_node = open[0]
    for node in open:
      if(node.f < min_node.f):
        min_node = node
    
    if min_node.isSolution:
      return min_node, count

    open.remove(min_node)
    child = None
    if(min_node.left is not None):
      child = min_node.left
      current_cost = min_node.g  + 1
      if(child in open):
        if child.g <= current_cost:
          continue
      elif child in closed:
        if child.g <= current_cost:
          continue
        closed.remove(child)
        open.append(child)
      else:
        open.append(child)
        child.h = heuristic2(child.state)
      child.g = current_cost

    if(min_node.right is not None):
      child = min_node.right
      current_cost = min_node.g + 1 
      if(child in open):
        if child.g <= current_cost:
          continue
      elif child in closed:
        if child.g <= current_cost:
          continue
        closed.remove(child)
        open.append(child)
      else:
        open.append(child)
        child.h = heuristic2(child.state)
        child.g = current_cost

    if(min_node.down is not None):
      child = min_node.down
      current_cost = min_node.g + 1
      if(child in open):
        if child.g <= current_cost:
          continue
      elif child in closed:
        if child.g <= current_cost:
          continue
        closed.remove(child)
        open.append(child)
      else:
        open.append(child)
        child.h = heuristic2(child.state)
      child.g = current_cost
    
    if(min_node.up is not None):
      child = min_node.up
      current_cost = min_node.g + 1
      if(child in open):
        if child.g <= current_cost:
          continue
      elif child in closed:
        if child.g <= current_cost:
          continue
        closed.remove(child)
        open.append(child)
      else:
        open.append(child)
        child.h = heuristic2(child.state)
      child.g = current_cost
    count = count + 1
    closed.append(min_node)
  return None, count

def printSolution(root, count):
  stack = []
  while(root != None):
    stack.insert(0, root)
    root = root.parent
  for board in stack:
    print_board_state(board.state)
    print(" \n")
  print("Number of moves: " + str(len(stack) - 1))
  print("Number of states enqueued: " + str(count))

def create_move_tree():
  state = []
  for i in sys.argv:
    if(len(i) == 1):
      state.append(i)

  x = 0
  root = create_node(state, x)

  if sys.argv[1] == "bfs":
    solution_node, count = bfs(root)
    if solution_node is None:
      print("No solution Found")
    printSolution(solution_node, count)
  elif sys.argv[1] == "ids":
    solution_node, count = IDS(root)
    if solution_node is None:
      print("No solution Found")
    printSolution(solution_node, count)
  elif sys.argv[1] == "astar1":
    solution_node, count = a_star1(root)
    if solution_node is None:
      print("No solution Found")
    printSolution(solution_node, count)
  elif sys.argv[1] == "astar2":
    solution_node, count = a_star2(root)
    if solution_node is None:
      print("No solution Found")
    printSolution(solution_node, count)
  else:
    print("Error: could not find matching function call")
    print(sys.argv)

def swap(state, x, y):
  temp = state[x]
  state[x] = state[y]
  state[y] = temp
  return state

def create_node(state, depth=0, parent=None):
  if not state:
    return

  root = Node(state, depth, parent)
  root_state = state.copy()

  if(root.depth > 10):
    return

  if root.empty_index == 0:
    root.right = create_node(swap(root_state.copy(), 0, 1), depth + 1, root)
    root.down = create_node(swap(root_state.copy(), 0, 4), depth + 1, root)
  elif root.empty_index == 1:
    root.left = create_node(swap(root_state.copy(), 1, 0), depth + 1, root)
    root.down = create_node(swap(root_state.copy(), 1, 4), depth + 1, root)
    root.right = create_node(swap(root_state.copy(), 1, 2), depth + 1, root)
  elif root.empty_index == 2:
    root.left = create_node(swap(root_state.copy(), 2, 1), depth + 1, root)
    root.down = create_node(swap(root_state.copy(), 2, 6), depth + 1, root)
  elif root.empty_index == 3:
    root.up = create_node(swap(root_state.copy(), 3, 0), depth + 1, root)
    root.right = create_node(swap(root_state.copy(), 3, 4), depth + 1, root)
    root.down = create_node(swap(root_state.copy(), 3, 6), depth + 1, root)
  elif root.empty_index == 4:
    root.up = create_node(swap(root_state.copy(), 4, 1), depth + 1, root)
    root.left = create_node(swap(root_state.copy(), 4, 3), depth + 1, root)
    root.down = create_node(swap(root_state.copy(), 4, 7), depth + 1, root)
    root.right = create_node(swap(root_state.copy(), 4, 5), depth + 1, root)
  elif root.empty_index == 5:
    root.up = create_node(swap(root_state.copy(), 5, 2), depth + 1, root)
    root.left = create_node(swap(root_state.copy(), 5, 4), depth + 1, root)
    root.down = create_node(swap(root_state.copy(), 5, 8), depth + 1, root)
  elif root.empty_index == 6:
    root.up = create_node(swap(root_state.copy(), 6, 3), depth + 1, root)
    root.right = create_node(swap(root_state.copy(), 6, 7), depth + 1, root)
  elif root.empty_index == 7:
    root.left = create_node(swap(root_state.copy(), 7, 6), depth + 1, root)
    root.up = create_node(swap(root_state.copy(), 7, 4), depth + 1, root)
    root.down = create_node(swap(root_state.copy(), 7, 8), depth + 1, root)
  elif root.empty_index == 8:
    root.left = create_node(swap(root_state.copy(), 8, 7), depth + 1, root)
    root.up = create_node(swap(root_state.copy(), 8, 5), depth + 1, root)
  return root
  
if __name__ == "__main__":
  create_move_tree()

