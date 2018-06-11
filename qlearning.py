import pickle
import random
import numpy as np

class QLearningForMaze():
  def __init__(self, maze):
    #初期戦略の設定
    initialstrategy = np.ones((maze.shape[0], maze.shape[1], 4), dtype=np.float64)
    for i in range(maze.shape[0]):
      for j in range(maze.shape[1]):
        #up
        if i-1 > 0:
          initialstrategy[i][j][0] = np.nan if maze[i-1][j] == 1 else 1
        else:
          initialstrategy[i][j][0] = np.nan
        #right
        if j+1 < maze.shape[1]:
          initialstrategy[i][j][1] = np.nan if maze[i][j+1] == 1 else 1
        else:
          initialstrategy[i][j][1] = np.nan
        #down
        if i+1 < maze.shape[0]:
          initialstrategy[i][j][2] = np.nan if maze[i+1][j] == 1 else 1
        else:
          initialstrategy[i][j][2] = np.nan
        #left
        if j-1 > 0:
          initialstrategy[i][j][3] = np.nan if maze[i][j-1] == 1 else 1
        else:
          initialstrategy[i][j][3] = np.nan
        if maze[i][j] == 3 or maze[i][j] == 1:
          initialstrategy[i][j] = np.array([np.nan, np.nan, np.nan, np.nan])
    #戦略決定値の設定
    self.initialstrategy = initialstrategy.copy()
    self.Q = np.random.random_sample(initialstrategy.shape)*initialstrategy.copy()*30
    #初期位置の設定
    self.startpos = np.array([0,0], dtype=np.int32)
    x = np.array(np.where(maze == 2))
    self.startpos[0] = x[0]
    self.startpos[1] = x[1]
    self.InitializePosition()

  def InitializePosition(self):
    self.x = self.startpos.copy()
  
  def DecideStrategy(self, epsilon):
    #decide strategy by epsilon-greedy method
    if random.random() < epsilon:
      pi = np.nan_to_num(self.initialstrategy[self.x[1],self.x[0]])
      pi /= np.sum(pi)
      strategy = np.random.choice(4, p=pi)
    else:
      strategy = np.nanargmax(self.Q[self.x[1],self.x[0]])
    return strategy
  
  def CalcReward(self, x, maze):
    reward = 0
    if maze[x[1], x[0]] == 3:
      #ゴールした場合の報酬
      reward = 1000
    else:
      #行きどまり時のペナルティ
      if list(self.Q[x[1],x[0]]).count(np.nan) == 3:
        reward = -1000
    return reward
  
  def CalcNextX(self, strategy):
    directions = np.array([(0,-1),(1,0),(0,1),(-1,0)])
    return self.x + directions[int(strategy)]
  
  def UpdateQParameter(self, maze, alpha, gumma, strategy):
    nextx = self.CalcNextX(strategy)
    R = self.CalcReward(nextx, maze)
    item2 = self.Q[self.x[1],self.x[0],int(strategy)]
    if maze[nextx[1],nextx[0]] == 3:
      self.Q[self.x[1],self.x[0],int(strategy)] += alpha*(R-item2)
    else:
      item1 = gumma*np.nanmax(self.Q[nextx[1],nextx[0]])
      self.Q[self.x[1],self.x[0],int(strategy)] += alpha*(np.nansum(np.array([R, item1, -item2])))
  
  def Update(self, maze, alpha, gumma, epsilon):
    strategy = self.DecideStrategy(epsilon)
    self.UpdateQParameter(maze, alpha, gumma, strategy)
    #update agent position
    self.x = self.CalcNextX(strategy)

def main():
  with open('mazedata.pickle', 'rb') as f:
    maze = pickle.load(f)
    agent = QLearningForMaze(maze)

    learningnum = 10000 #試行回数
    history_x = []
    history_y = []
    alpha = 0.1
    gamma = 0.9
    epsilon = 0.5
    for i in range(learningnum):
      agent.InitializePosition()
      while maze[agent.x[1],agent.x[0]] != 3:
        #エージェントの軌跡を格納
        history_x.append(agent.x[0])
        history_y.append(agent.x[1])
        #エージェントを更新(位置とパラメータ)
        agent.Update(maze, alpha, gamma, epsilon)
      #エージェントの軌跡を格納
      history_x.append(agent.x[0])
      history_y.append(agent.x[1])
      epsilon -= 0.5/learningnum
    
  #エージェントの移動履歴をファイルに出力
  with open('qlearnresult.pickle', 'wb') as f:
    pickle.dump((history_x, history_y), f)
  
  #最終的なQ値を出力(各位置での最大のQ値を持つ方略)
  resultQ = np.zeros((agent.Q.shape[:-1]))
  for i in range(agent.Q.shape[0]):
    for j in range(agent.Q.shape[1]):
      if not np.all(np.isnan(agent.Q[i][j])):
        resultQ[i,j] = np.nanargmax(agent.Q[i][j])
      else:
        resultQ[i, j] = np.nan
  print(resultQ)

if __name__ == '__main__':
  main()