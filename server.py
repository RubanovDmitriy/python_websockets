import asyncio
import websockets

from models import SumArgs


def summ(i, j) -> str:
    result = abs(i) + abs(j)
    if result > 100:
        return "Your sum is bigger than 100"
    return f"Your sum is: {result}"


async def echo(websocket, path):
    async for message in websocket:
        sum_model = SumArgs.model_validate_json(message)
        result = summ(i=sum_model.first_arg, j=sum_model.second_arg)
        await websocket.send(result)


start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
