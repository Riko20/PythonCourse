#Write function which make requests on https://httpbin.org/ with using few threads

import threading
import time
from urllib import request

def make_request(url, i):
    print('Thread {} starting making req to: {}'.format(i, url))
    resp = request.urlopen(url)
    print('Thread {} finished: {}'.format(i, resp))

def by_threads():
    url = 'https://httpbin.org/'
    for i in range(3):
        t = threading.Thread(target=make_request, args= (url, i))
        t.start()
        t.join()

by_threads()


#Create an queue of tasks. Create workers who will do tasks from queue and perform them. Quantity workers - optional argument, Quantity of tasks: opt. 1 worker == 1 thread
import queue


def worker(i):
    print('Worker {} start doing his best'.format(i))
    while True:
        task = q.get()
        if task == None:
            break
        do_task(task)
        print('Worker {}. It done'.format(i))
        q.task_done()


def do_task(task):
    print('Task is not very hard: {}'.format(task))
    time.sleep(1)


q = queue.Queue()

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.setDaemon(True)
    t.start()

for exc in range(5):
    q.put(exc)
q.join()


print('what next?')


###### ASYNCIO ######  There is a pull of urls, create 2-3 functions which will do requests to this url. Requests must be create by means of asyncio

import asyncio


async def req1(url):
    print('Req1 is executing: {}'.format(url))
    resp = request.urlopen(url)
    await asyncio.sleep(0)
    print('Req1 is done: {}'.format(resp))


async def req2(url):
    print('Req2 is executing: {}'.format(url))
    resp = request.urlopen(url)
    await asyncio.sleep(0)
    print('Req2 is done: {}'.format(resp))


async def handler():
    urls = ['http://ip-api.com/json', 'https://httpbin.org/']

    for url in urls:
        futures = [asyncio.ensure_future(req1(url)), asyncio.ensure_future(req2(url))]

    await asyncio.wait(futures)


loop = asyncio.new_event_loop()
loop.run_until_complete(handler())
loop.close()
