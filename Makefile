.PHONY: build up down clean logs

run:
	docker-compose build
	docker-compose up -d

logs:
	docker-compose logs -f

clean:
	docker-compose down -v
	docker system prune -f
	docker volume prune -f
