# ansible-readlogs
## Pre-requisites
- Authenticate all serverXX.quiz.example.neustar hosts using ssh keys
- Create inventory file for above servers

## What this playbook does
- Replaces empty microseconds lines with 0 ms 
- Runs a python script on remote hosts to calculate mean and standard deviation
- Returns the values as standard output like below
```bash
  TASK [readlog : Get stdout or stderr from the output] 
    ok: [dev1] => {
        "python_result.stdout_lines": [
            "Mean: 9.45",
            "Standard Deviation: 2.94066319051"
        ]
```

# How to run the playbook
```bash
- git clone https://github.com/shashibuyakar/ansible-readlogs.git
- cd ansible-readlogs
- ansible-playbook -i inventory  main.yml
```
