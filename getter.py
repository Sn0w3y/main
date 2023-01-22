from handler import add_register

# Register address to read from
register = 35121
# File name of the requestor
requestor = "getter.py"

# Add the register address and requestor name to the queue
try:
    add_register(register, requestor)
except Exception as e:
    print("An error occurred while trying to add the register: ", e)
