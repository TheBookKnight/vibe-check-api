.PHONY: start stop
start:
	@docker compose up --detach

stop:
	@docker compose down