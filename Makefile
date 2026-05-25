up:
	docker compose up --build

down:
	docker compose down

restart:
	docker compose down
	docker compose up --build

logs:
	docker compose logs -f

backend:
	docker compose exec backend-api bash

agent:
	docker compose exec ai-agent bash

seed:
	docker compose exec backend-api python seed_products.py

ps:
	docker ps

clean:
	docker system prune -f
