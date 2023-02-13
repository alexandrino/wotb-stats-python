import responses
import pytest

from urllib3.exceptions import NewConnectionError

from src.handlers.player_indexer import get_stats, fetch_data


@responses.activate
def test_get_stats_success():
    responses.add(responses.GET, "http://localhost/account/info/?application_id=11112&account_id=11113",
                  json={"status": "ok"}, status=200)

    result = get_stats({}, {})
    assert result.get("status_code") == 200
    assert result.get("body") == '"{\\"status\\": \\"ok\\"}"'


def test_get_stats_success(mocker):
    mocker.patch("src.handlers.player_indexer.fetch_data", side_effect=Exception('mocked error'))
    result = get_stats({}, {})
    assert result.get("status_code") == 500
    assert result.get("body") == {'status': 'server error'}


@responses.activate
def test_fetch_data_success():
    responses.add(responses.GET, "http://localhost/account/info/?application_id=11112&account_id=11113",
                  json={"status": "ok"}, status=200)

    result = fetch_data()   
    assert result.json() == {"status": "ok"}


