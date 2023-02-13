invoke_player_indexer:
	sls invoke local -f player_indexer

install:
	pip install -r requirements.txt

test:
	pytest --cov=. --cov-report term-missing --cov-fail-under=72 -vv ./tests