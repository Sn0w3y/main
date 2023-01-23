import pymodbus

# Create a Modbus RTU client
client = pymodbus.client.sync.ModbusSerialClient(method='rtu', port='COM1', timeout=1)

# Connect to the device
client.connect()
