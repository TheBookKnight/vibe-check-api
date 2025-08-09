# Vibe Check API
An LLM-powered content moderation service built with [FastAPI](https://fastapi.tiangolo.com/).

## Getting Started

Will require [uv package manager](https://docs.astral.sh/uv/getting-started/installation/) and [Docker Desktop](https://docs.docker.com/desktop/).

You can install [MongoDB Compass](https://www.mongodb.com/try/download/compass) to observe data changes.

1. Setup the virtual environment and install dependencies.
```bash
uv venv .venv
uv sync
```

2. Start the virtual environment. 
```bash
source .venv/bin/activate
```

3. Run the app! It's running locally on port 8000.
```bash
fastapi dev src/main.py
```

4. View the API docs (provided by [SwaggerUI](https://github.com/swagger-api/swagger-ui)) in http://127.0.0.1:8000/docs

5. Run the MongoDB container so you can test its API commands
```bash
# runs the MongoDB container
make start/db 

# stops the MongoDB container
make stop/db 
```
