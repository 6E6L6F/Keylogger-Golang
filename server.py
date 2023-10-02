from websockets.server import serve 
import asyncio
from datetime import datetime


def write_data_user(name , data):
    date = str(datetime.today().year) + "/" + str(datetime.today().month) + "/" + str(datetime.today().day)
    time = str(datetime.today().hour) + ":" + str(datetime.today().minute) + ":" + str(datetime.today().second)
    with open("data/"+name+".txt" , 'a+') as file:
        file.write(f"{date} - {time} : Message : {data}\n")

async def echo(websocket):
    async for message in websocket:
        ip , port = websocket.remote_address
        write_data_user(ip , str(message))                

async def main():
    async with serve(echo , "0.0.0.0" , 8989):
        await asyncio.Future()


asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()
