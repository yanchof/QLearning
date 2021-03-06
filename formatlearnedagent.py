import pickle
import numpy as np

def main():
  with open('learnedagent.pickle', 'rb') as f:
    history = pickle.load(f)

  with open('learnedagent.txt', 'w') as f:
    for i in range(len(history[0])):
      f.write('{},{}\n'.format(history[0][i], history[1][i]))

if __name__ == '__main__':
  main()