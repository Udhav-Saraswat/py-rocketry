import asyncio
from rocketry import Rocketry
from rocketry.conds import every
import logging

app = Rocketry(config=
               {"task_execution": "async"})

@app.task(every('10 seconds', based="finish"))
async def do_permanently():
    "This runs for really long time"
    print("Task-running")

async def main():
    sched = asyncio.create_task(app.serve())
    await asyncio.wait([sched])

if __name__ == "__main__":
    # Print Rocketry's logs to terminal
    logger = logging.getLogger("rocketry.task")
    logger.addHandler(logging.StreamHandler())

    # Run both applications
    asyncio.run(main())