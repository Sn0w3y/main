import worker
import TaskCreator
import connector
import time

# Set the slave address
slave = 247

# Set the cycle time
cycle_time = 1000

# Create ReadTasks for multiple registers
task1 = ReadTask(script1.client, 35121, Priority.HIGH, slave)
task2 = ReadTask(script1.client, 35122, Priority.HIGH, slave)
task3 = ReadTask(script1.client, 35123, Priority.LOW, slave)

# Add the tasks to the worker
worker = ModbusWorker()
worker.add_read_task(task1)
worker.add_read_task(task2)
worker.add_read_task(task3)

# Collect the next set of tasks and execute them
try:
    worker.on_before_process_image()
    worker.on_execute_write()
except Exception as e:
    print(f'Error occured during execution: {e}')
    script1.client.close()
    exit()

# Store the result in a variable
result1 = task1.result
result2 = task2.result
result3 = task3.result

# Do something with the data
print("Data from register 35121:", result1.registers[0])
print("Data from register 35122:", result2.registers[0])
print("Data from register 35123:", result3.registers[0])

# Close the connection
script1.client.close()
