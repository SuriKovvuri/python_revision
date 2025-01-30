import time

def task1():
    print("Task 1 started")
    time.sleep(2)  # Simulating a task taking 2 seconds
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(3)  # Simulating a task taking 3 seconds
    print("Task 2 completed")

# Sequential execution
task1()
task2()



import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # Simulating a task taking 2 seconds
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(3)  # Simulating a task taking 3 seconds
    print("Task 2 completed")

async def main():
    # Run tasks concurrently
    await asyncio.gather(task1(), task2())

# Run the event loop
asyncio.run(main())


# Key Differences
# Feature	Synchronous	Asynchronous
# Execution	Tasks are executed one by one.	Tasks can run concurrently.
# Waiting	A task blocks the program.	A task doesn't block others.
# Performance	Slower for I/O-heavy tasks.	Faster for I/O-heavy tasks.


