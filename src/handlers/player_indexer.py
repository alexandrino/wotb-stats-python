import json
import requests
import os

from src.common.log import logger

api_endpoint = os.environ.get("API_ENDPOINT")
app_id = os.environ.get("APP_ID")
account_id = os.environ.get("ACCOUNT_ID")

def fetch_data():
    url = f"{api_endpoint}/account/info/?application_id={app_id}&account_id={account_id}"
    return requests.get(url)


def get_stats(event, context):
    logger.debug("get_stats.start")
    try:
        body = fetch_data()
        response = {
            "statusCode": 200,
            "body": json.dumps(body.text)
        }
        logger.info("get_stats.success")
        return response

    except Exception as exc:
        logger.error(f"get_stats.error {exc}")
        return {
            "statusCode": 500,
        }


    return response