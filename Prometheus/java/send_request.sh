#!/bin/bash

URL="http://localhost:9091/heavy"

while true; do
  curl -X GET "$URL"
  echo "\nRequest sent at: $(date)"
  sleep 1
done
