from src.services.player.repository.dynamodb import save_stats

def save_player_stats(stats = None) -> bool:
  return save_stats(stats)
