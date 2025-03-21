up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

rebuild:
	docker-compose build --no-cache

exec-bash:
	docker-compose exec app bash

clear:
	docker-compose down -v --remove-orphans

test-db-init:
	uv run alembic upgrade head

test:
	uv pytest tests/

test-db-reset:
	docker-compose down -v && docker-compose up -d db
