import asyncio
from pymodbus.client import ModbusSerialClient as ModbusClient
from asyncio import Queue
from multiprocessing import Array

# create a modbus client instance
client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600)

# create a shared memory array
register_address = Array('i', [0], lock=True)

async def modbus_handler(register_address_value, result_queue):
    print(f"register address value: {register_address_value}")
    # Connect to the modbus device
    await client.connect()
    if client.connect():
        print("Connected to the device successfully.")
        result = await client.read_holding_registers(register_address_value, 1, unit=247)
        await result_queue.put(result.registers[0])
    else:
        print("Failed to connect to the device.")
    # Close the connection
    await client.close()


async def main():
    # create the result queue
    result_queue = Queue()
    # start the listener task
    task = asyncio.create_task(listener(result_queue))
    while True:
        while register_address[0] == 0:
            await asyncio.sleep(0.1)
        # get the register address from the shared memory array
        register_address_value = register_address[0]
        # reset the register address value
        register_address[0] = 0
        # start a new task for the register address
        asyncio.create_task(modbus_handler(register_address_value, result_queue))


async def listener(result_queue):
    while True:
        try:
            # try to get the result immediately
            result = await result_queue.get_nowait()
            # process the result
            print(result)
        except asyncio.QueueEmpty:
            # if the queue is empty, wait for a while
            await asyncio.sleep(0.1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())