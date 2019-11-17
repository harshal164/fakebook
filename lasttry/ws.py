#!/usr/bin/env python3
import asyncio
import websockets

connected = set()

async def hello(ws,path):
    connected.add(ws)
    while True:
        name = await ws.recv()
        greeting = f"{name}"
        await asyncio.wait([w.send(greeting) for w in connected])

st_serv = websockets.serve(hello,port=8765)

asyncio.get_event_loop().run_until_complete(st_serv)
asyncio.get_event_loop().run_forever()
