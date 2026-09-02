class GridEnvironment:
    # def __init__(
    #     self,
    #     rows,
    #     cols,
    #     obstacles=None,
    # ):
    #     self.rows = rows
    #     self.cols = cols

    #     self.obstacles = set(
    #         obstacles or []
    #     )
    
    def __init__(
        self,
        rows,
        cols,
        obstacles=None,
        terrain_costs=None,
    ):
        self.rows = rows
        self.cols = cols

        self.obstacles = set(
            obstacles or []
        )

        self.terrain_costs = dict(
            terrain_costs or {}
        )
                
    # Valid Cell Detection
    def is_inside(self, state):
        row, col = state

        return (
            0 <= row < self.rows
            and 0 <= col < self.cols
        )
        
    def is_obstacle(self, state):
      return state in self.obstacles
    
    def is_valid(self, state):
      return (
          self.is_inside(state)
          and not self.is_obstacle(state)
      )
      
    # 4 directional: UP, DOWN, LEFT, RIGHT
    def neighbors(self, state):
      row, col = state

      directions = [
          (-1, 0),
          (1, 0),
          (0, -1),
          (0, 1),
      ]

      result = []

      for row_delta, col_delta in directions:
          neighbor = (
              row + row_delta,
              col + col_delta,
          )

          if self.is_valid(neighbor):
              # result.append(
              #     (neighbor, 1.0)
              # )
              
              # We assume the Edge cost to be the cost of entering the destination cell.
              result.append(
                (
                  neighbor,
                  self.cost(neighbor),
                )
              )

      return result
    
    def __contains__(self, state):
      return self.is_valid(state)
    
    def cost(self, state):
      return self.terrain_costs.get(
          state,
          1.0,
      )