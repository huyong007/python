#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'huyong'

'''
async web Application.
'''


import time
import json
import os
import asyncio
from aiohttp import web
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>hello,world</h1>', headers={'content-type': 'text/html'})


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('sever started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
