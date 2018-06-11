class Agent {
  int seek;
  private int x;
  private int y;

  ArrayList<Integer> xhistory;
  ArrayList<Integer> yhistory;

  Agent() {
    seek = 0;
    xhistory = new ArrayList<Integer>();
    yhistory = new ArrayList<Integer>();
  }

  public void LoadAgentData(String path) {
    String[] lines = loadStrings(path);
    for (int i = 0; i < lines.length; i++) {
      String items[] = lines[i].split(",", 0);
      int x = Integer.parseInt(items[0]);
      int y = Integer.parseInt(items[1]);
      xhistory.add(x);
      yhistory.add(y);
    }
  }

  public void Show(int size) {
    int x = xhistory.get(seek);
    int y = yhistory.get(seek);

    fill(200, 100, 100);
    rect(size*x+10, size*y+10, size, size);
  }

  public void Update() {
    seek += 1;
    if (seek >= xhistory.size()) {
      seek = 0;
    }
  }
}