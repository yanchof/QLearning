import numpy as np
import random
import pickle
import sys

'''
Simple maze is constructed by walls, blanks, start position, goal position.
Theire representaions are below.

blanks: 0
walls:  1
start position: 2
goal position: 3
'''
def GenerateSimpleMaze(width, height, startpos):
  maze = np.ones((height, width), dtype=np.int32)
  maze[startpos[1], startpos[0]] = 2
  x = startpos
  Digging(maze, x)
  return maze

def Digging(maze, x):
  directions = np.array([(0,1),(1,0),(0,-1),(-1,0)])
  height = maze.shape[0]
  width = maze.shape[1]

  random.shuffle(directions)
  for direction in directions:
    target = x + direction*2

    if 0 <= target[0] < width and 0 <= target[1] < height:
      target_value = maze[target[1], target[0]]

      if target_value == 1:
        maze[target[1], target[0]] = 0
        maze[(x+direction)[1], (x+direction)[0]] = 0
        Digging(maze, target)

def SetGoalOnMaze(maze, startpos):
  visited = np.zeros_like(maze)
  visited += maze
  goallist = SearchAllGoal(maze, visited, startpos, 0)
  goalpos = max(goallist, key=lambda x: x[1])
  maze[goalpos[0][1], goalpos[0][0]] = 3

def SearchAllGoal(maze, visited, x, depth):
  visited[x[1],x[0]] = 1
  directions = np.array([(0,1),(1,0),(0,-1),(-1,0)])
  goallist = list()
  goalflag = True
  for direction in directions:
    target = x + direction
    if visited[target[1], target[0]] == 0:
      goallist.extend(SearchAllGoal(maze, visited, target, depth+1))
      goalflag = False
  if goalflag:
    goallist.append((x, depth))
  return goallist

if __name__ == '__main__':
  '''
  usage: command <width> <height> <x> <y>
  '''
  if len(sys.argv) == 5:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    x = int(sys.argv[3])
    y = int(sys.argv[4])
    maze = GenerateSimpleMaze(width, height, (x,y))
    SetGoalOnMaze(maze, (1,1))
    print(maze)
    with open('mazedata.pickle', mode='wb') as f:
      pickle.dump(maze, f)