class ReadTask:
    def __init__(self, device, register, priority, slave):
        self.device = device
        self.register = register
        self.priority = priority
        self.slave = slave

    def execute(self):
        # code to read data from the device using pymodbus
        result = self.device.read_holding_registers(self.register, 1, unit=self.slave)
        print(result.registers)
