import click
from loguru import logger
import random
import time

logging_map = {
        "TRACE":" A really detailed trace info about your app",
        "DEBUG": "This should be paid atention to track your logic",
        "INFO": "Take a look into this info. It may be relevant",
        "SUCCESS": "A successfull logic occured",
        "WARNING": "Hey! this could not happend but the app will proceed",
        "ERROR": "No!No! It shall not proceed! Computer says no!",
        "CRITICAL": "Oh snap! this will fall into hell!!!!!",
}


@click.command()
def pyrandlog(logs: int=10_000):

    for _ in range(logs):
        level, message = random.choice(list(logging_map.items()))
        logger.log(level, message)
        rand_sleep = random.randint(10,100) / 1_000
        time.sleep(rand_sleep)



if __name__ == "__main__":
    pyrandlog()
