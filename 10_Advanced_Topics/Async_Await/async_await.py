"""Async/await with asyncio."""
import asyncio, time
async def task(i):
    await asyncio.sleep(0.1)
    return i*i
async def main():
    results = await asyncio.gather(*(task(i) for i in range(5)))
    print(results)
if __name__ == "__main__":
    asyncio.run(main())
