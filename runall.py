from mythic import mythic
import asyncio
import argparse

mythic_username = "mythic_admin"
mythic_password = "mythic_admin"
mythic_serverip = "192.168.0.158"
mythic_serverport = 7443


async def main() -> asyncio.coroutines:

    # arg parse stuff
    parser = argparse.ArgumentParser(description='Runs a command on all Mythic callbacks.')
    parser.add_argument('-a', '--agent', required=True, help='The type of agent you want to run commands on')
    parser.add_argument('-t', '--task', default='shell', help='The task that you want to run. Default: shell')
    parser.add_argument('-c', '--command', required=True, help='The command you want to run')
    
    args = parser.parse_args()

    agent = args.agent
    tasking = args.task
    command = args.command
    
    try:
        print("[i] Connecting to Mythic Instance...")

        mythic_instance = await mythic.login(
            username = mythic_username,
            password = mythic_password,
            server_ip = mythic_serverip,
            server_port = mythic_serverport,
            timeout = -1
        )

        print("[+] Connected to Mythic Instance.")
        print(f"[i] Selected task: {tasking}")
        print(f"[i] Selected agent: {agent}")

        ids = []

        callbacks = await mythic.get_all_active_callbacks(
            mythic = mythic_instance
        )

        for i in range(len(callbacks)):
            if ((callbacks[i]['payload']['payloadtype']['name']) == agent):
            # print(callbacks)
                ids.append(callbacks[i]['display_id'])
        
        if len(ids) == 0:
            print(f"[-] ERROR! There are no callbacks of type {agent}")
            exit()

        for i in range(len(ids)):
            print(f"[i] Running '{tasking}' task with '{command}' command on callback ID {ids[i]}")
            task = await mythic.issue_task(
                mythic = mythic_instance,
                command_name = tasking,
                parameters = command,
                callback_display_id = ids[i],
                timeout = 10,
                wait_for_complete = False
            )

    except Exception as e:
        print(str(e))

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())