#!/bin/bash

URL="http://localhost:8081"

while true; do
  curl -X GET "$URL"
  echo "\nRequest sent at: $(date)"
  sleep 1
done
