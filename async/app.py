import asyncio
import random

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def hello_world(request):
    return JSONResponse({'hello': 'world'})


async def wait(request):
    wait_millis = random.randint(10, 30)
    await asyncio.sleep(wait_millis / 1000.0)
    return JSONResponse({'wait': wait_millis})


async def blocked(request):
    rounds = random.randint(10000, 100000)
    for _ in range(rounds):
        pass
    return JSONResponse({'rounds': rounds})


app = Starlette(debug=True, routes=[
    Route('/', hello_world),
    Route('/wait', wait),
    Route('/blocked', blocked),
])
