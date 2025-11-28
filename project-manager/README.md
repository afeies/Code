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