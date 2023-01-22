import logging
from handler import add_register
import time

logger = logging.getLogger("getter")

# Register address to read from
register = 35135
register1 = 35136
# File name of the requestor
requestor = "getter2.py"

while True:
    # Add the register address and requestor name to the queue
    add_register(register, requestor)
    add_register(register1, requestor)
    time.sleep(1)
