#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request and store response body in a temporary file
response=$(mktemp)
curl -s -o "$response" "$1"

# Calculate and display the size of the response body in bytes
size=$(stat -c %s "$response")
echo "$size"

# Clean up temporary file
rm "$response"
