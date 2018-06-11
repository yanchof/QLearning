import pickle
import numpy as np

def main():
  with open('mazedata.pickle', 'rb') as f:
    maze = pickle.load(f)

  with open('mazedata.txt', 'w') as f:
    f.write('{},{}\n'.format(maze.shape[0], maze.shape[1]))
    for i,row in enumerate(maze):
      for j,col in enumerate(row):
        f.write('{},{},{}\n'.format(i, j, maze[i][j]))

if __name__ == '__main__':
  main()