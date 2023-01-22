import time
from multiprocessing import Array
from handler import register_address
import asyncio
from handler import main

def getter():
    # get the register address from somewhere
    register = 35121
    print(f"register address: {register}")
    register_address[0] = register


if __name__ == "__main__":
    while True:
        getter()
        time.sleep(5)



