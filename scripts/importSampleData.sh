#!/bin/bash
echo "Importing for Vibe Check API..."

echo "Importing users..."
mongoimport --host mongo --db content --collection users --file ../db/messages.json --jsonArray

echo "Importing messages..."
mongoimport --host mongo --db content --collection messages --file ../db/users.json --jsonArray
