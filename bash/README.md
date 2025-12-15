# Notes
- cp <target> <destination>
- mv <target> <destination>

- flag: something you add to a command to change what it does

- pipe operator: takes output of first command and uses it as input to another command
    - without pipe: command prints output to terminal

1. filtering lines with grep
- ls | grep ".txt"

- process: a program that is currently running
    - VS Code running is a process
2. counting lines with wc -l
- ps aux | wc -l
    - ps aux: lists all running processes
        - ps: process status
            - by itself only shows processes in your current shell
            - 
    - wc -l: counts lines