from handler import add_register
import threading
from queue import Queue

register_queue = Queue()

# Register address to read from
register = 35121
# File name of the requestor
requestor = "getter.py"

# Add the register address and requestor name to the queue
add_register(register, requestor)

register_queue.join()
thread.join()
