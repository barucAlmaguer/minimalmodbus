import minimalmodbus
import time

instr = minimalmodbus.Instrument('COM4',1)
instr.serial.baudrate = 9600

def print():
    instr

def blink(pin, count, s):
    for i in range(0,count):
        instr.write_bit(pin,1)
        time.sleep(s)
        instr.write_bit(pin,0)
        time.sleep(s)

def readJoystick():
    return instr.read_registers(0,2,4)