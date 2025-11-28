#!/bin/bash

# get current timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# store the first argument in a variable called COMMAND
COMMAND=$1
PROJECT_NAME=$2

# e.g. ./project-manager.sh new blog
if [ "$COMMAND" = "new" ]; then
    # create new directory blog
    mkdir "$PROJECT_NAME"
    # create new file blog/README.md
    touch "$PROJECT_NAME"/README.md
    # write # blog to blog/README.md
    echo "# $PROJECT_NAME" > "$PROJECT_NAME"/README.md

    echo "Created project: $PROJECT_NAME"
    # stop script
    exit 0
fi

if [ "$COMMAND" = "list" ]; then
    echo "Existing projects:"
    ls -d */ | grep -v "logs"
    exit 0
fi

if [ "$COMMAND" = "delete" ]; then
    rm -r "$PROJECT_NAME"
    echo "Deleted project: $PROJECT_NAME"
    exit 0
fi

# write to log file (append)
echo "[$TIMESTAMP] Project Manager started" >> logs/history.log

# print confirmation to terminal
echo "Logged start time"