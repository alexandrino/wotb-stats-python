from pydantic import BaseModel


class PlayerStats(BaseModel):
  spotted: int
  max_frags_tank_id: int
  hits: int
  frags: int
  max_xp: int
  max_xp_tank_id: int
  wins: int
  losses: int
  capture_points: int
  battles: int
  damage_dealt: int
  damage_received: int
  max_frags: int
  shots: int
  frags8p: int
  xp: int
  win_and_survived: int
  survived_battles: int
  dropped_capture_points: int


