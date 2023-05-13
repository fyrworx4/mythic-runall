# mythic-runall

A Python script that runs a single command over multiple callbacks in Mythic through the GraphQL interface. Updated for Mythic v3.0.0.

## Installation
Clone the repository:
```bash
git clone https://github.com/fyrworx4/mythic-runall.git
```
Install Mythic Python library:
```
pip3 install mythic
```

## Setup

Edit `runall.py` with your Mythic server's IP address and admin username/password.

```
mythic_username = "mythic_admin"
mythic_password = "mythic_admin"
mythic_serverip = "10.128.10.239"
mythic_serverport = 7443
```

## Usage

```
usage: runall.py [-h] -a AGENT -c COMMAND

Runs a command on all Mythic callbacks.

options:
  -h, --help            show this help message and exit
  -a AGENT, --agent AGENT
                        The agent of the callbacks
  -c COMMAND, --command COMMAND
                        The command you want to run
```

## Example

To run `whoami` on all callbacks that use the `merlin` agent:
```bash
python3 runall.py -a merlin -c 'whoami'
```