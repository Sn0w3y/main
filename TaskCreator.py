class ReadTask:
    def __init__(self, device, register, priority):
        self.device = device
        self.register = register
        self.priority = priority

    def execute(self):
        # code to read data from the device using pymodbus
        result = self.device.read_holding_registers(self.register, 1)
        print(result.registers)

    def get_execute_duration(self):
        # expected duration of the read operation
        return 200

# Create a ReadTask
task1 = ReadTask(client, 1, Priority.HIGH)
task2 = ReadTask(client, 2, Priority.LOW)
