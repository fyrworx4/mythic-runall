# mythic-runall

A quick Python script that uses the Mythic REST API to run a command on all callbacks in a Mythic instance.

## Installation
```bash
git clone https://github.com/fyrworx4/mythic-runall.git
pip3 install mythic
```

## Setup

Edit `runall.py` with your Mythic server's IP address and admin username/password.

```
mythic = mythic_rest.Mythic(
        username="mythic_admin",
        password="mythic_admin",
        server_ip="192.168.0.158",
        server_port="7443",
        ssl=True,
        global_timeout=-1,
    )
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