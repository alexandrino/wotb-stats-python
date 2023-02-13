import json
import requests
import os

from src.common.log import logger


def fetch_data():
    api_endpoint = os.environ.get("API_ENDPOINT", "http://localhost")
    app_id = os.environ.get("APP_ID", 11112)
    account_id = os.environ.get("ACCOUNT_ID", 11113)

    url = f"{api_endpoint}/account/info/?application_id={app_id}&account_id={account_id}"
    return requests.get(url)


def get_stats(event, context):
    logger.debug("get_stats.start")

    try:
        body = fetch_data()
        response = {
            "status_code": 200,
            "body": json.dumps(body.text)
        }
        logger.info("get_stats.success")
        return response

    except Exception as exc:
        logger.error(f"get_stats.error {exc}")

        return {
            "status_code": 500,
            "body": {"status": "server error"}
        }
