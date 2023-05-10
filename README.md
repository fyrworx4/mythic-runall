# mythic-runall

A quick Python script that uses the Mythic REST API to run a command on all callbacks in a Mythic instance.

## Installation
```bash
git clone https://github.com/fyrworx4/mythic-runall.git
pip3 install mythic
```

## Usage

```bash
usage: script.py [-h] -a AGENT -c COMMAND

Runs a command on all Mythic callbacks.

options:
  -h, --help            show this help message and exit
  -a AGENT, --agent AGENT
                        The agent of the callbacks
  -c COMMAND, --command COMMAND
                        The command you want to run
```