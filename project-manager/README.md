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

## Additional notes
- machine: Mac laptop
    - the hardware + environment you're working on
- OS: macOS
    - the software that runs that harware
- kernel: XNU
    - the core of that OS
- shell: Bash
    - the interface you use to talk to the OS

- Bash is a shell
    - a shell is a program that lets you talk to os
    - works naturally on Unix-like OSes
    - PowerShell for Windows
- Unix is an OS
    - mostly historial but shapes every major OS we see today
    - everything is a file: disks, terminals, processes, etc.
- Unix-like OSes follow Unix design
    - Linux distributions, macOS are Unix-like
    - Windows is not Unix-like
- os, kernel
    - masOS, XNU kernel
    - iOS, XNU kernel
    - Windows, NT kernel
    - Linux distributions (Ubuntu, Fedora, Arch), Linux kernel
- vim: terminal text editor
    - runs inside terminal on top of Bash
- some commands are built into the shell
    - cd, echo, export, etc.
- other commands are external programs
    - vim, ls, git, python3, node, gcc, docker, etc.