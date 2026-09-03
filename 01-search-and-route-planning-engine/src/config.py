from dataclasses import dataclass

@dataclass
class GridExperimentConfig:
  rows: int
  cols: int
  obstacle_probability: float
  start: tuple
  goal: tuple
  trials: int = 1