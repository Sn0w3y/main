import logging
from handler import add_register

logger = logging.getLogger("getter")

# Register address to read from
register = 35123
register1 = 35121
# File name of the requestor
requestor = "getter2.py"

# Add the register address and requestor name to the queue
add_register(register, requestor)
add_register(register1, requestor)
