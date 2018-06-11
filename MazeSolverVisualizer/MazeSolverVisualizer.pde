import controlP5.*;

//UI周り
ControlP5 LoadMazeFileButton, LoadAgentFileButton;
ControlP5 PlayButton, PauseButton, ResetButton;
//迷路とエージェントのデータ
boolean loadmazeflag = false;
Maze maze;
boolean loadagentflag = false;
Agent agent;
//再生周り
boolean playflag = false;

void setup() {
  size(580, 420);
  frameRate(60);
  textFont(createFont("Arial", 20), 20);
  textAlign(CENTER);

  //迷路データ読み込み用ボタン
  LoadMazeFileButton = new ControlP5(this);
  LoadMazeFileButton.addButton("LoadMaze")
    .setLabel("LoadMaze")
    .setPosition(450, 10)
    .setSize(100, 40)
    .setColorCaptionLabel(color(255));
  //エージェントデータ読み込みボタン
  LoadAgentFileButton = new ControlP5(this);
  LoadAgentFileButton.addButton("LoadAgent")
    .setLabel("LoadAgent")
    .setPosition(450, 60)
    .setSize(100, 40)
    .setColorCaptionLabel(color(255));
  //再生ボタン
  PlayButton = new ControlP5(this);
  PlayButton.addButton("Play")
    .setLabel("Play")
    .setPosition(450, 130)
    .setSize(70, 40)
    .setColorCaptionLabel(color(255));
  //一時停止ボタン
  PauseButton = new ControlP5(this);
  PauseButton.addButton("Pause")
    .setLabel("Pause")
    .setPosition(450, 180)
    .setSize(70, 40)
    .setColorCaptionLabel(color(255));
  //リセットボタン
  ResetButton = new ControlP5(this);
  ResetButton.addButton("Reset")
    .setLabel("Reset")
    .setPosition(450, 230)
    .setSize(70, 40)
    .setColorCaptionLabel(color(255));

  maze = new Maze();
  agent = new Agent();
}

void draw() {
  background(255);
  
  fill(255);
  rect(10, 10, 390, 390);

  //迷路の描画
  if (loadmazeflag) {
    maze.Show();
  }
  //エージェントの描画
  if (loadagentflag) {
    agent.Show(maze.GetPanelSize());
  }
  //エージェントの位置の更新
  if (playflag) {
    agent.Update();
  }
}

void controlEvent(ControlEvent theEvent) {
  if (theEvent.getController().getName() == "LoadMaze") {
    selectInput("Select a maze data file.", "LoadMazeFile");
  }
  if (theEvent.getController().getName() == "LoadAgent") {
    selectInput("Select a agent data file.", "LoadAgentFile");
  }
  if (theEvent.getController().getName() == "Play") {
    Play();
  }
  if (theEvent.getController().getName() == "Pause") {
    Pause();
  }
  if (theEvent.getController().getName() == "Reset") {
    Reset();
  }
}

void LoadMazeFile(File selection) {
  if (selection == null) {
    println("Success");
  } else {
    String path = selection.getAbsolutePath();
    maze.LoadMazeData(path);
    loadmazeflag = true;
  }
}

void LoadAgentFile(File selection) {
  if (selection == null) {
    println("Success");
  } else {
    String path = selection.getAbsolutePath();
    agent.LoadAgentData(path);
    loadagentflag = true;
    println("loaded");
  }
}

void Play() {
  playflag = true;
}

void Pause() {
  playflag = false;
}

void Reset() {
  agent.seek = 0;
}