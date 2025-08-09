## Starts database for testing Python app with MongoDB
.PHONY: start/debug stop/debug
start/db:
	@docker run mongo:latest --name mongo --detach 27017:27017

stop/db:
	@docker stop mongo && docker rm mongo

## Starts and stops the local Docker environment for the vibe-check-api project with database
.PHONY: start/local stop/local
start/local:
	@docker compose up --detach

stop/local:
	@docker compose down