class Maze {
  private int width;
  private int height;
  private int[][] data;
  private int size;

  Maze() {
    this.width = 0;
    this.height = 0;
    this.data = null;
    size = 0;
  }

  Maze(int width, int height) {
    this.width = width;
    this.height = height;
  }

  public void LoadMazeData(String path) {
    String[] lines = loadStrings(path);
    //迷路のサイズを取得 (width, height)
    String strsizeparam[] = lines[0].split(",", 0);
    this.width = Integer.parseInt(strsizeparam[0]);
    this.height = Integer.parseInt(strsizeparam[1]);
    //迷路データの領域を確保
    data = new int[this.height][];
    for (int i = 0; i < this.height; i++) {
      data[i] = new int[this.width];
    }
    //迷路データの登録
    for (int i = 1; i < this.height*this.width+1; i++) {
      String items[] = lines[i].split(",", 0);
      int x = Integer.parseInt(items[1]);
      int y = Integer.parseInt(items[0]);
      int kind = Integer.parseInt(items[2]);
      data[y][x] = kind;
    }

    this.size = 400 / this.width;
  }

  public int GetPanelSize() {
    return this.size;
  }

  public void Show() {
    for (int i = 0; i < this.height; i++) {
      for (int j = 0; j < this.width; j++) {
        stroke(0);
        switch(data[i][j]) {
          case 0:
            noFill();
            break;
          case 1:
            fill(180);
            break;
          case 2:
            fill(0);
            text("S",this.size*(j+0.5)+10,this.size*(i+0.5)+10);
            noFill();
            break;
          case 3:
            fill(0);
            text("G",this.size*(j+0.5)+10,this.size*(i+0.5)+10);
            noFill();
            break;
        }
        rect(this.size*j+10, this.size*i+10, this.size, this.size);
      }
    }
  }
}