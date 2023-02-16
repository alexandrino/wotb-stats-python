import boto3
import time
import json

from src.models.player_stats import PlayerStats
from src.common.log import logger

dynamo_client  =  boto3.resource("dynamodb")
player_table = dynamo_client.Table("player_stats")


def save_stats(player_id: str, stats: PlayerStats) -> bool:

  data = {
    "player_id": player_id,
    "created_at": str(time.time()),
    "stats": json.dumps(stats)
  }

  try:
    player_table.put_item(Item=data)
    logger.debug("save_stats.put_item.success")
    return True
  except Exception as exc:
    logger.exception(f"save_stats.put_item.error {exc}")
    return False



