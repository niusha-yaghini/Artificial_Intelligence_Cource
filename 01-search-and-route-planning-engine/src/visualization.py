import matplotlib.pyplot as plt

def print_grid(
  grid,
  start=None,
  goal=None,
  path=None,
  explored=None,
):
  path = set(path or [])
  explored = set(explored or [])

  for row in range(grid.rows):
    symbols = []

    for col in range(grid.cols):
      state = (row, col)

      if state == start:
        symbol = "S"

      elif state == goal:
        symbol = "G"

      elif state in grid.obstacles:
        symbol = "#"

      elif state in path:
        symbol = "*"

      elif state in explored:
        symbol = "o"

      else:
        symbol = "."

      symbols.append(symbol)

    print(" ".join(symbols))
        
        
def plot_grid(
  grid,
  start=None,
  goal=None,
  path=None,
  explored=None,
):
  fig, ax = plt.subplots()

  ax.set_xlim(
    -0.5,
    grid.cols - 0.5
  )

  ax.set_ylim(
    -0.5,
    grid.rows - 0.5
  )

  ax.set_xticks(range(grid.cols))
  ax.set_yticks(range(grid.rows))

  ax.grid(True)

  ax.invert_yaxis()
  
  path = set(path or [])
  
  explored = set(explored or [])

  for row in range(grid.rows):
    for col in range(grid.cols):

      state = (row, col)

      if state in grid.obstacles:
        ax.text(
          col,
          row,
          "#",
          ha="center",
          va="center",
          fontsize=18,
        )

      elif state == start:
        ax.text(
          col,
          row,
          "S",
          ha="center",
          va="center",
          fontsize=18,
        )

      elif state == goal:
        ax.text(
          col,
          row,
          "G",
          ha="center",
          va="center",
          fontsize=18,
        )
      
      elif state in path:
        ax.text(
          col,
          row,
          "*",
          ha="center",
          va="center",
          fontsize=18,
        )
        
      elif state in explored:
        ax.text(
          col,
          row,
          "o",
          ha="center",
          va="center",
          fontsize=14,
        )

  plt.show()