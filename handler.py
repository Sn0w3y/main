import threading
from queue import Queue
from pymodbus.client import ModbusSerialClient as ModbusClient
from pymodbus.exceptions import ModbusException
import logging
import time

logger = logging.getLogger("getter")
logger.setLevel(logging.INFO)

# Create a StreamHandler to redirect the output to the console
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

# Modbus connection parameters
port = '/dev/ttyUSB0'
baudrate = 9600
stopbits = 1
parity = 'N'
unit_id = 247

# Create a queue to store register addresses and requestor names
register_queue = Queue()

# Create Modbus client
client = ModbusClient(method='rtu', port=port, baudrate=baudrate, stopbits=stopbits, parity=parity, timeout=1)

# Connect to the Modbus device
connection = client.connect()

modbus_lock = threading.Lock()

def read_register(register):
    modbus_lock.acquire()
    try:
        # Read data from the specified register
        result = client.read_holding_registers(register, 1, unit=unit_id)
        # Return the data as a list
        return result.registers
    except ModbusException as e:
        print(e)
        return None
        modbus_lock.release()
    finally:
        modbus_lock.release()

def add_register(register, requestor):
    register_queue.put((register, requestor))

# Create a thread to continuously read data from the Modbus device
def read_thread():
    while True:
        # Get the next register address and requestor name from the queue
        register, requestor = register_queue.get()
        # Read data from the Modbus device
        data = read_register(register)
        # Print the data with requestor name
        logger.info("Data from register {} requested by {}: {}".format(register, requestor, data))
        # Wait for 1 second before reading the next register address
        time.sleep(1)
        # Mark the task as done
        register_queue.task_done()

# Start the thread
thread = threading.Thread(target=read_thread)
thread.start()