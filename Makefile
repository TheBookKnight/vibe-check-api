## Starts database for testing Python app with MongoDB
.PHONY: start/debug stop/debug import/db
start/db:
	@docker compose up database --detach
	@make import/db
	
stop/db:
	@docker compose down database

import/db:
	@echo "Importing sample data into MongoDB..."
	@chmod +x scripts/importSampleData.sh
	@docker exec mongo scripts/importSampleData.sh

## Starts and stops the local Docker environment for the vibe-check-api project with database
.PHONY: start/local stop/local
start/local:
	@docker compose up --detach
	@make import/db

stop/local:
	@docker compose down