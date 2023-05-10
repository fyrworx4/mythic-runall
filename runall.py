from mythic import mythic_rest
from sys import exit
from os import system
import asyncio
import json
import argparse


async def scripting(agent, command):
    
    # sample login
    mythic = mythic_rest.Mythic(
        username="mythic_admin",
        password="mythic_admin",
        server_ip="192.168.0.158",
        server_port="7443",
        ssl=True,
        global_timeout=-1,
    )
    print("[+] Logging into Mythic")
    await mythic.login()

    print(f"[i] Running '{command}' on all {agent} agents")

    try:
        # get all callbacks in some weird output
        all_tasks = await mythic.get_all_tasks_and_responses_grouped_by_callback()
        output = all_tasks.to_json()['raw_response']['output']

        # for each callback ID, run some command
        for i in range(len(output)):
            if output[i]['payload_type'] == agent:

                # extracting the callback ID from get_all_tasks_and_responses_grouped_by_callback() output
                id = int(output[i]['id'])

                # create a new Callback object for each ID, create a new task that runs some command
                
                callback = mythic_rest.Callback(id=id)
                task = mythic_rest.Task(
                    callback=callback, command="shell", params=command
                )

                # perform the task
                await mythic.create_task(task)
                print(f"[+] Callback ID {id}: Successfully ran '{command}'")

    except Exception as e:
        print(str(e))

# everything below here is expected as a staple at the end of your program
# this launches the functions asynchronously and keeps the program running while long-running tasks are going
async def main():
    parser = argparse.ArgumentParser(description='Runs a command on all Mythic callbacks.')
    parser.add_argument('-a', '--agent', required=True, help='The agent of the callbacks')
    # parser.add_argument('-t', '--task', default='shell', help='The task to run. Default = shell')
    parser.add_argument('-c', '--command', required=True, help='The command you want to run')

    args = parser.parse_args()
    agent = args.agent
    command = args.command


    await scripting(agent, command)
    try:
        while True:
            pending = asyncio.all_tasks()
            plist = []
            for p in pending:
                if p._coro.__name__ != "main" and p._state == "PENDING":
                    plist.append(p)
            if len(plist) == 0:
                exit(0)
            else:
                await asyncio.gather(*plist)
    except KeyboardInterrupt:
        pending = asyncio.Task.all_tasks()
        for t in pending:
            t.cancel()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
