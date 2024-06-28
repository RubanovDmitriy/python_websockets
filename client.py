import asyncio
import websockets
import json


async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            event = None

            try:
                first_arg = input("Enter first argument or 'q' to exit: ")
                if first_arg == 'q':
                    break
                second_arg = input("Enter second argument or 'q' to exit: ")
                if second_arg == 'q':
                    break
                event = {'first_arg': int(first_arg), 'second_arg': int(second_arg)}

            except ValueError:
                print('Please enter integer')
            if event:
                await websocket.send(json.dumps(event))
                response = await websocket.recv()
                print(f"Server replied: {response}")


asyncio.get_event_loop().run_until_complete(send_message())
