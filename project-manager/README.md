I am learning bash, so I made a mini project, a project manager. Here are my notes:

# Create folder
- mkdir ...
    - make directory: creates a new folder
- cd ...
    - change directory: moves you into a different folder
- mkdir logs
- ls
    - list: shows all files and folders in the current directory

# Create script
- touch ...
    - create new empty file
- code ...
    - open a file or folder
    - had to go in command palette and install code path

## Add script header
- #!/bin/bash
    - shebang: tells the system to run this script with Bash interpreter
- echo ...
    - print text to terminal

## Make file executable
- chmod +x ...
    - chmod: change mode, change file permissions
    - +x: add executable permission
    - tell OS to treat the file like a program you can run

## Run the script
- ./filename
    - run a file in the current directory

# Add timestamp logging
- date
    - default format: Fri Nov 28 01:15:41 EST 2025
- date +"%Y-%m-%d %H:%M:%S"
    - custom format
- $(...)
    - command substitution: runs a command inside another command and returns its output
- '>'
    - overwrite file
- '>>'
    - append to file (add at the end)

# Add Commands
- new
- list
- delete

## Add script arguments
- $1: the first argument after the script name
- $2: the second argument
    - allow the script to behave differently based on user input

## Add conditional logic
`if [...]; then
    # commands
fi`
- exit 0
    - stops the script from running further
        - 0 means success
        - non-zero values indicate error
- cat ...
    - concatenate: prints contents of file in terminal

## Add "list" command
- ls -d */
    - list only directories (trailing / means show only folders)
- grep -v "logs"
    - grep: filter text
    - -v: invert match (remove lines containing ...)

## Add "delete" command
- rm -r ...
    - rm: remove file
    - -r: recursive, required to delete folders