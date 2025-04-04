
# https://www.geeksforgeeks.org/asyncio-in-python/
import asyncio

async def fun():
    print("Hi this is async function")
    await asyncio.sleep(1)
    print("Nice to meet you")
    await asyncio.sleep(1)
    print("Thank you!")
asyncio.run(fun())

import time

def fun():
    print("Hi this is a normal function")
    time.sleep(1)  # Replaces asyncio.sleep
    print("Nice to meet you")
    time.sleep(1)
    print("Thank you!")

fun()  # Call the function normally


import asyncio

async def fun():
    print("Hi this is suri")
    await asyncio.sleep(1)
    print("From Vijayawada..")
    await asyncio.sleep(1)
    print("Thank you")
asyncio.run(fun())



import asyncio 
async def fn():
     
    print("one")
    await asyncio.sleep(1)
    await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
 
async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
asyncio.run(fn())




import asyncio
async def fn():
    task=asyncio.create_task(fn2())
    print("one")
    #await asyncio.sleep(1)
    #await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
 
async def fn2():
    #await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
     
asyncio.run(fn())


# I/O-bound tasks using asyncio.sleep()
import asyncio
async def func1():
	print("Function 1 started..")
	await asyncio.sleep(2)
	print("Function 1 Ended")


async def func2():
	print("Function 2 started..")
	await asyncio.sleep(3)
	print("Function 2 Ended")


async def func3():
	print("Function 3 started..")
	await asyncio.sleep(1)
	print("Function 3 Ended")


async def main():
	L = await asyncio.gather(
		func1(),
		func2(),
		func3(),
	)
	print("Main Ended..")
asyncio.run(main())
