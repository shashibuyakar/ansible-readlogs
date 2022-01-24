# ansible-readlogs
## Pre-requisites
- Tested on ansible [core 2.12.1] and python version = 3.8.1
- Authenticate all serverXX.quiz.example.neustar hosts using ssh keys

## What this playbook does
- Replaces empty microseconds lines with 0 ms 
- Runs a python script on remote hosts to calculate mean and standard deviation of application timings
- Returns the values as standard output like below
```bash
  TASK [readlog : Get stdout or stderr from the output] 
    ok: [localhost] => {
        "python_result.stdout_lines": [
            "Mean: 9.45",
            "Standard Deviation: 2.94066319051"
        ]
```

## How to run the playbook
```bash
- git clone https://github.com/shashibuyakar/ansible-readlogs.git
- cd ansible-readlogs
- ansible-playbook -i inventory  main.yml
```
