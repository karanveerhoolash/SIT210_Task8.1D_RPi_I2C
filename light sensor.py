import smbus
import time

BH1750_sensor = 0x23

received_add = 0x20

bus = smbus.SMBus(1)

def Light():
    address = bus.read_i2c_block_data(BH1750_sensor,received_add)
    val = Light_intensity(address)
    return val
    
def Light_intensity(address):
    result = (address[1] + (256 * address[0])) / 1.2  # proper conversion
    return (result)
    
def Action():
    while True:
        level = Light()  // read value of light
        print(level)
        
        if (level >= 1402):
            print("Too Bright")
        elif (level >= 302 and level < 1402):
            print("Bright")
        elif (level >= 92) and (level < 302):
            print("Medium")
        elif (level >= 30) and (level < 92):
            print("dark")
        elif (level < 30):
            print("too dark")
            
        time.sleep(0.3)
        
Action()