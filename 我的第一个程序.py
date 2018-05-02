import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(1)
    return  web.Response(text='fertig')

async def hallo(request):
    await asyncio.sleep(2)
    text='hallo %s'%request.match_info['name']
    return web.Response(text=text)

async def init(loop):
    app=web.Application(loop=loop)
    app.router.add_get('/',index)#这里传入的参数request就是'/'
    app.router.add_get('/hallo/{name}',hallo)#这里传入的参数就是'/hallo/{name}',其中name是一个根据用户的输入来判定的
    srv=await loop.create_server(app.make_handler(),'127.0.0.1',8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
